#!/usr/bin/env python3
"""
Script to update CSS in all lecture pages to include dark-mode.css
"""

import os
import re
import glob

def update_lecture_css():
    """Update all lecture QMD files to include dark-mode.css."""
    lecture_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(lecture_dir)
    
    lecture_files = glob.glob("lecture*.qmd")
    
    for filename in lecture_files:
        print(f"Processing {filename}...")
        
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Check if the file already has dark-mode.css
        if '../dark-mode.css' in content:
            print(f"  {filename} already has dark-mode.css")
            continue
        
        # Replace single CSS with multiple CSS
        updated_content = re.sub(
            r'---\n(.*?)format:\s*\n\s*html:\s*\n\s*css:\s*\.\.\/styles\.css\s*\n---',
            '---\n\\1format:\n  html:\n    css: \n      - ../styles.css\n      - ../dark-mode.css\n---',
            content,
            flags=re.DOTALL
        )
        
        # Write the updated content
        if updated_content != content:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(updated_content)
            print(f"  Updated CSS in {filename}")
        else:
            print(f"  No changes needed in {filename}")

if __name__ == "__main__":
    update_lecture_css()
    print("CSS updated in all lecture files.")
