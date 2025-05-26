#!/usr/bin/env python3
"""
Script to update the navigation styling in all lecture QMD files.
"""

import os
import re
import glob

def update_navigation_styling():
    """Update navigation link styling in all lecture QMD files."""
    lecture_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(lecture_dir)
    
    print(f"Working in directory: {os.getcwd()}")
    
    lecture_files = glob.glob("lecture*.qmd")
    print(f"Found {len(lecture_files)} lecture files")
    
    modified_count = 0
    
    for filename in sorted(lecture_files):
        print(f"Processing {filename}...")
        
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Check if the file has navigation at top
        if '::: {.lecture-nav style=' in content:
            print(f"  Found navigation in {filename}")
            # Update the styling to match the new CSS
            updated_content = content.replace(
                '::: {.lecture-nav style="display: flex; justify-content: space-between; margin-bottom: 2rem; padding-bottom: 1rem; border-bottom: 1px solid #ddd;"}',
                '::: {.lecture-nav style="display: flex; justify-content: space-between; margin-bottom: 2rem; padding-bottom: 1rem; border-bottom: 1px solid var(--border-color);"}'
            )
            
            if updated_content != content:
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(updated_content)
                print(f"  Updated navigation styling in {filename}")
                modified_count += 1
            else:
                print(f"  No changes needed for {filename}")
        else:
            print(f"  No navigation found in {filename}")
    
    print(f"Updated navigation styling in {modified_count} files.")

if __name__ == "__main__":
    update_navigation_styling()
    print("Navigation styling updated in all lecture files.")
