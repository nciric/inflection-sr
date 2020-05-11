#[macro_use]
extern crate lazy_static;

use bzip2::read::BzDecoder;
use regex::Regex;
use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::env;
use std::fs::File;
use std::io::{prelude::*, BufReader};
use std::time::{Instant};

#[derive(Serialize, Deserialize, Debug)]
struct Entity {
    #[serde(default)]
    labels: HashMap<String, HashMap<String, String>>
}

fn is_serbian_cyrillic(input: &String) -> bool {
    lazy_static! {
        static ref RE: Regex = Regex::new(r"^[\p{Cyrillic} ]+$").unwrap();
    }
    RE.is_match(input)
}

fn extract_serbian_name(data: &str) -> Option<String> {
    let entity: Option<Entity> = match serde_json::from_str(data) {
        Ok(elem) => Some(elem),
        Err(_) => None,
    };

    if let Some(elem) = entity {
        if let Some(block) = elem.labels.get("sr") {
            if let Some(value) = block.get("value") {
                return Some(value.clone());
            }
        }
    }

    None
}

fn process_file(input_file_name: &str, output_file_name: &str) {
    // Open input.
    let file = File::open(input_file_name).expect("Error opening file.");
    let decoder = BzDecoder::new(file);
    let reader = BufReader::new(decoder);

    // Create output.
    let mut output = File::create(output_file_name).expect("Couldn't create output file");

    // Lets see how long it will take.
    let time_start = Instant::now();
    let mut line_count: u64 = 0;

    for line in reader.lines() {
        let mut line = line.expect("Couldn't read line.");
        if line.ends_with(',') {
            line.pop();
        }
        let result = extract_serbian_name(&line);
        if let Some(name) = result {
            if is_serbian_cyrillic(&name) {
                writeln!(output, "{}", name).expect("Failed to write line.");
            }
        }

        line_count += 1;
        if line_count % 1_000 == 0 {
            println!("Processed {} lines", line_count);
        }
    }

    let duration = time_start.elapsed();
    println!("Total time to complete: {:?}", duration);
}

fn main() {
    let args: Vec<String> = env::args().collect();

    let default_file: String = "latest-all.bz2".to_string();
    let default_output: String = "../entities.txt".to_string();

    match args.len() {
        1 => process_file(&default_file, &default_output),
        2 => process_file(&args[1], &default_output),
        3 => process_file(&args[1], &args[2]),
        _ => panic!("Too many arguments. Specify input and output files only."),
    }
}