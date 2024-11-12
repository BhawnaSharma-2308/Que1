Approach - 
Identify the Query Patterns: Read the patterns of interest from a query file (data/to_select.tsv). Each pattern will be stored as a separate value, assuming one pattern per line.
Filter the Big File: Use a Linux command to handle the unknown column position for the patterns and pipe the data to Python.
Python Script: Process the piped data, matching the patterns regardless of column order.

Command - 
zcat q1_data.tsv.gz | python pattern_selector.py to_select.tsv > matched_lines.tsv
