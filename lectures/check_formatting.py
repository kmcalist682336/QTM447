#!/usr/bin/env python3
import os
import re
import glob

def check_list_formatting(file_path):
    """
    Check if lists in the file have proper blank lines before them.
    Returns a list of line numbers where issues might exist.
    """
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Skip YAML front matter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2]
    
    lines = content.split('\n')
    problem_lines = []
    
    # Pattern for list items (both ordered and unordered)
    list_pattern = re.compile(r'^\s*[-*+]\s+.*$|^\s*\d+\.\s+.*$')
    
    for i, line in enumerate(lines):
        # Skip first line or empty lines
        if i == 0 or not line.strip():
            continue
        
        # Check if current line is a list item
        if list_pattern.match(line):
            # Check if previous line is empty
            if lines[i-1].strip():
                # Previous line is not empty, possible formatting issue
                problem_lines.append(i + 1)  # +1 for 1-based line numbering
    
    return problem_lines

def main():
    summary_dir = os.path.dirname(os.path.abspath(__file__)) + '/summaries'
    summary_files = glob.glob(f"{summary_dir}/Lecture*Summary.qmd")
    
    # If no files found, try a different path
    if not summary_files:
        summary_dir = '/home/kmcalist/ClassSites/QTM447/lectures/summaries'
        summary_files = glob.glob(f"{summary_dir}/Lecture*Summary.qmd")
    
    issues_found = False
    
    print("Checking Markdown formatting in lecture summary files...")
    print("Looking for lists without proper blank lines before them...\n")
    
    for file_path in sorted(summary_files):
        file_name = os.path.basename(file_path)
        problem_lines = check_list_formatting(file_path)
        
        if problem_lines:
            issues_found = True
            print(f"[ISSUE] {file_name}: Potential list formatting issues at lines: {', '.join(map(str, problem_lines))}")
        else:
            print(f"[OK] {file_name}: No list formatting issues detected")
    
    if issues_found:
        print("\nSuggested fix:")
        print("For each identified issue, add a blank line before the list starts.")
        print("Example:")
        print("Before:\nThis is a paragraph.\n- List item 1\n- List item 2")
        print("\nAfter:\nThis is a paragraph.\n\n- List item 1\n- List item 2")
    else:
        print("\nAll lecture summary files have proper formatting for lists!")

if __name__ == "__main__":
    main()
