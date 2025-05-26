#!/usr/bin/env python3
"""
Script to remove dark-mode.css from all lecture pages
"""
import os
import re
import glob

def remove_dark_mode():
    """Remove dark-mode.css from all lecture QMD files."""
    lecture_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(lecture_dir)
    
    lecture_files = glob.glob("lecture*.qmd")
    
    for filename in lecture_files:
        print(f"Processing {filename}...")
        
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Check if the file has dark-mode.css
        if '../dark-mode.css' in content:
            # Replace multiple CSS with single CSS
            updated_content = re.sub(
                r'css: \n\s*- \.\./styles\.css\n\s*- \.\./dark-mode\.css',
                'css: ../styles.css',
                content
            )
            
            # Write the updated content
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(updated_content)
            print(f"  Removed dark-mode.css from {filename}")
        else:
            print(f"  {filename} doesn't have dark-mode.css")

if __name__ == "__main__":
    remove_dark_mode()
    print("Removed dark-mode.css from all lecture files.")
