""" Parses xml file from https://dumps.wikimedia.org/srwiki/latest/srwiki-latest-pages-meta-current.xml.bz2 , extracts
unique words, in Serbian alphabet, and writes them to TSV file (count, word).
We don't actually care about XML parsing, so a line reader should be enough."""

import re
import time


def serbian_cyrillic_match(input, search=re.compile(r'[^А-Ша-ш]').search):
    """ Serbian Cyrillic matcher. """
    return not bool(search(input))


# Keep words and counts.
result = {}

print('Start processing...')
line_count = 0
start_time = time.time()

input_file = "srwiki-latest-pages-meta-current.xml"
with open(input_file, 'rt', encoding="utf-8") as infile:
    for line in infile:
        # "Segment" the line by whitespace
        parts = line.split()
        for part in parts:
            lowercased_word = part.lower()
            # For each word, check if it's in Serbian Cyrillic.
            if serbian_cyrillic_match(lowercased_word):
                count, full_list = result.get(lowercased_word, [0, set()])
                # Since we lowercased, preserve all shapes we encountered so far.
                full_list.add(part)
                result.update({lowercased_word: [count + 1, full_list]})
        line_count += 1
        if line_count % 1000000 == 0:
            print('Processed', line_count, 'lines in', time.time() - start_time, 's')
infile.close()

output_file = "word_frequency_table.tsv"
outfile = open(output_file, 'w+t', encoding="utf-8")
# Sort results by word counts - item[1][0].
sorted_results = {k: v for k, v in sorted(result.items(), key=lambda item: item[1][0], reverse=True)}
for key, value in sorted_results.items():
    count = value[0]
    full_list = ','.join(value[1])
    outfile.write(str(count) + '\t' + key + '\t' + full_list + '\n')
outfile.close()
