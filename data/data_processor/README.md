To use:
1. Download files from (wikimedia site)[https://dumps.wikimedia.org/srwiki/latest/].
2. You probably want srwiki-latest-pages-meta-current.xml.bz2 and srwiki-latest-pages-articles.xml.bz2
3. Decompress them in data/ folder (or enywhere else)
4. cargo run --release [input glob] [output_file]

Resulting tab separated file will be sorted by word frequency.