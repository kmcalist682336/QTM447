#!/usr/bin/env python3
"""
Script to move navigation buttons from bottom to top in all lecture pages.
"""

import os
import re
import glob

def move_navigation():
    """Move navigation buttons from bottom to top in all lecture QMD files."""
    lecture_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(lecture_dir)
    
    print(f"Working in directory: {os.getcwd()}")
    
    lecture_files = glob.glob("lecture*.qmd")
    print(f"Found {len(lecture_files)} lecture files")
    
    for filename in lecture_files:
        print(f"Processing {filename}...")
        
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Check if the file has navigation at bottom
        # The pattern needs to match this exact structure with newlines and spacing
        nav_pattern = r'::: {\.lecture-nav style="display: flex; justify-content: space-between; margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #ddd;"}\s*<div>\s*\[.*?\]\(.*?\)\s*</div>\s*<div>\s*\[.*?\]\(.*?\)\s*</div>\s*:::'
        nav_match = re.search(nav_pattern, content, re.DOTALL)
        
        if nav_match:
            nav_content = nav_match.group(0)
            # Remove navigation from bottom
            content_without_nav = content.replace(nav_content, '')
            
            # Update nav styling for top placement
            top_nav = nav_content.replace(
                'margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #ddd;',
                'margin-bottom: 2rem; padding-bottom: 1rem; border-bottom: 1px solid #ddd;'
            )
            
            # Find position after YAML header
            yaml_end = content.find('---', 3) + 3
            
            # Insert navigation after YAML header
            updated_content = content[:yaml_end] + '\n\n' + top_nav + content[yaml_end:].replace(nav_content, '')
            
            # Write the updated content
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(updated_content)
            print(f"  ✅ Moved navigation to top in {filename}")
        else:
            print(f"  ❌ No standard navigation found in {filename}")

if __name__ == "__main__":
    move_navigation()
    print("Navigation moved to top in all lecture files.")
