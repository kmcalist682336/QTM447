#!/usr/bin/env python3
import os
import re
import glob
import shutil

def fix_list_formatting(file_path):
    """
    Fix lists in the file by adding blank lines before them where needed.
    Returns the number of fixes made.
    """
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Preserve the YAML front matter
    yaml_front_matter = ""
    content_body = content
    
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            yaml_front_matter = "---" + parts[1] + "---"
            content_body = parts[2]
    
    lines = content_body.split('\n')
    fixed_lines = []
    fixes_count = 0
    
    # Pattern for list items (both ordered and unordered)
    list_pattern = re.compile(r'^\s*[-*+]\s+.*$|^\s*\d+\.\s+.*$')
    
    for i, line in enumerate(lines):
        # If it's the first line or already preceded by an empty line, just add it
        if i == 0 or not lines[i-1].strip():
            fixed_lines.append(line)
        # If current line is a list item
        elif list_pattern.match(line):
            # If previous line is not empty, insert an empty line
            if lines[i-1].strip():
                fixed_lines.append('')  # Add empty line
                fixes_count += 1
            fixed_lines.append(line)
        else:
            fixed_lines.append(line)
    
    # Reconstruct the file
    fixed_content = yaml_front_matter + '\n'.join(fixed_lines)
    
    # Create a backup of the original file
    backup_path = file_path + '.bak'
    shutil.copy2(file_path, backup_path)
    
    # Write the fixed content to the original file
    with open(file_path, 'w') as f:
        f.write(fixed_content)
    
    return fixes_count

def main():
    summary_dir = '/home/kmcalist/ClassSites/QTM447/lectures/summaries'
    summary_files = glob.glob(f"{summary_dir}/Lecture*Summary.qmd")
    
    total_fixes = 0
    files_fixed = 0
    
    print("Fixing Markdown formatting in lecture summary files...")
    print("Adding blank lines before lists where needed...\n")
    
    for file_path in sorted(summary_files):
        file_name = os.path.basename(file_path)
        fixes = fix_list_formatting(file_path)
        
        if fixes > 0:
            files_fixed += 1
            total_fixes += fixes
            print(f"[FIXED] {file_name}: Made {fixes} formatting fixes")
        else:
            print(f"[UNCHANGED] {file_name}: No fixes needed")
    
    print(f"\nSummary: Fixed {total_fixes} formatting issues in {files_fixed} files.")
    print("Backup files with '.bak' extension have been created for all modified files.")
    print("You can now verify the changes and remove the backup files if satisfied.")

if __name__ == "__main__":
    main()
