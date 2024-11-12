""" :r! zcat q1_data.tsv.gz | head -n 10 | sed 's/^/\/\/ /' """
// transcript_id(s)	gene_id	length	effective_length	expected_count	TPM	FPKM	posterior_mean_count	posterior_standard_deviation_of_count	pme_TPM	pme_FPKM	TPM_ci_lower_bound	TPM_ci_upper_bound	TPM_coefficient_of_quartile_variation	FPKM_ci_lower_bound	FPKM_ci_upper_bound	FPKM_coefficient_of_quartile_variation
// 10904	10904	93.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0	0	0	0	0	0
// 12954	12954	94.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0	0	0	0	0	0
// 12956	12956	72.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0	0	0	0	0	0
// 12958	12958	82.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0	0	0	0	0	0
// 12960	12960	73.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0	0	0	0	0	0
// 12962	12962	72.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0	0	0	0	0	0
// 12964	12964	74.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0	0	0	0	0	0
// 12965	12965	82.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0	0	0	0	0	0
// 12967	12967	73.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0	0	0	0	0	0

""" :r! cat to_select.tsv | head -n 10 | sed 's/^/\/\/ /' """
$1 = to_select.tsv file 
// ENSG00000180353.10
// ENSG00000180596.7
// ENSG00000266379.6
// ENSG00000262561.1
// ENSG00000284999.1
// ENSG00000274641.1
// ENSG00000231441.1
// ENSG00000267655.1
// ENSG00000209082.1
// ENSG00000119446.13

import sys

def load_patterns(query_file):
    """Load patterns from the query file."""
    with open(query_file, 'r') as f:
        patterns = {line.strip() for line in f if line.strip()}
    return patterns

def match_line(line, patterns):
    """Check if any pattern matches any column in the line."""
    columns = line.strip().split('\t')
    return any(column in patterns for column in columns)

if __name__ == "__main__":
    # Load patterns from the query file
    query_file = sys.argv[1]
    patterns = load_patterns(query_file)

    # Read lines from stdin and output matching lines
    for line in sys.stdin:
        if match_line(line, patterns):
            print(line, end='')
""" 
This script will reaq1_data.tsv.gzd patterns from a query file (to_select.tsv), then reads lines from standard input (the large file, q1_data.tsv.gz piped in), and outputs lines that contain the specified patterns in any column
The script will be run with a cat linux command as,
zcat q1_data.tsv.gz | python3 pattern_selector.py to_select.tsv > matched_lines.tsv 
"""
