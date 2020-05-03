#[macro_use]
extern crate lazy_static;

use itertools::join;
use glob::glob;
use regex::Regex;
use std::collections::{HashMap, HashSet};
use std::env;
use std::fs::File;
use std::io::{prelude::*, BufReader};
use std::path;
use std::time::{Instant};

fn is_serbian_cyrillic(input: &String) -> bool {
    lazy_static! {
        static ref RE: Regex = Regex::new(r"[\p{Cyrillic}]+").unwrap();
    }
    RE.is_match(input)
}

// Keeps track of total count for the word, and saves all similar words (upper/lower case difference only).
type WordCountMap = HashMap<String, (u32, HashSet<String>)>;

fn count_words(file_name: path::PathBuf, word_count: &mut WordCountMap, line_count: &mut u64) {
    println!("Processing {:?}", file_name);
    let file = File::open(file_name).expect("Error opening file.");
    let reader = BufReader::new(file);

    for line in reader.lines() {
        let line = line.expect("Couldn't read line.");
        let parts: Vec<&str> = line.split(|c: char| !c.is_alphabetic()).collect();
        for part in parts {
            if part.is_empty() || !is_serbian_cyrillic(&String::from(part)) { continue }
            let lowercased_word = part.to_lowercase();
            if let Some(item) = word_count.get_mut(&lowercased_word) {
                item.0 += 1;  // Increment global count for this word.
                item.1.insert(String::from(part));  // Push full form of the word to the set.
            } else {
                let mut initial_set: HashSet<String> = HashSet::new();
                initial_set.insert(String::from(part));
                word_count.insert(lowercased_word, (1, initial_set));
            }
        }

        if *line_count % 1_000_000 == 0 {
            println!("Processed {} total lines", *line_count);
        }
        *line_count += 1;
    }
}

fn write_results(output_file: &str, word_count: &WordCountMap) {
    let mut output = File::create(output_file).expect("Couldn't create output file");

    // Copy to vector, so we can sort. Vector contains (String, (count, hashset))
    let mut word_count_vec: Vec<_> = word_count.iter().collect();
    word_count_vec.sort_by(|a, b| (a.1).0.cmp(&(b.1).0).reverse());
    for item in word_count_vec {
        let full_list = join(&(item.1).1, ", ");
        let count = (item.1).0;
        writeln!(output, "{}\t{}\t{}", count, item.0, full_list).expect("Failed to write line.");
    }
}

fn process_files(file_glob: &str, output_file: &str) {
    // Result goes here.
    let mut word_count: WordCountMap = HashMap::new();

    // Lets see how long it will take.
    let time_start = Instant::now();
    let mut line_count: u64 = 0;

    // Match the glob pattern, filtering out bad paths.
    for file_name in glob(file_glob).unwrap().filter_map(Result::ok) {
        count_words(file_name, &mut word_count, &mut line_count);
    }

    let duration = time_start.elapsed();
    println!("Total time to complete: {:?}", duration);

    write_results(output_file, &word_count);
}

fn main() {
    let args: Vec<String> = env::args().collect();

    let default_glob: String = "../*.xml".to_string();
    let default_output: String = "../word_frequency_table.tsv".to_string();

    match args.len() {
        1 => process_files(&default_glob, &default_output),
        2 => process_files(&args[1], &default_output),
        3 => process_files(&args[1], &args[2]),
        _ => panic!("Too many arguments. Specify input glob, and output file only."),
    }
}
