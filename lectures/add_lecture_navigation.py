#!/usr/bin/env python3
"""
Script to add navigation buttons to all lecture pages.
"""

import os
import re
import glob

def add_navigation_to_lectures():
    """Add previous and next navigation links to all lecture QMD files."""
    lecture_files = sorted(glob.glob("lecture[0-9]*.qmd") + glob.glob("lecture[0-9][0-9].qmd"))
    
    # Create a mapping of lecture numbers to file names
    lecture_map = {}
    for file in lecture_files:
        match = re.search(r'lecture(\d+)\.qmd', file)
        if match:
            lecture_num = int(match.group(1))
            lecture_map[lecture_num] = file
    
    # Sort the lecture numbers
    lecture_nums = sorted(lecture_map.keys())
    
    # Process each lecture file
    for i, lecture_num in enumerate(lecture_nums):
        filename = lecture_map[lecture_num]
        print(f"Processing {filename}...")
        
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Check if navigation is already present
        if "::: {.lecture-nav" in content:
            print(f"  Navigation already exists in {filename}")
            continue
        
        # Determine previous and next lecture numbers
        prev_num = lecture_nums[i-1] if i > 0 else None
        next_num = lecture_nums[i+1] if i < len(lecture_nums)-1 else None
        
        # Create navigation HTML
        nav_html = "\n\n::: {.lecture-nav style=\"display: flex; justify-content: space-between; margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #ddd;\"}\n"
        
        if prev_num:
            prev_file = lecture_map[prev_num]
            nav_html += f"<div>\n[← Previous: Lecture {prev_num}]({prev_file})\n</div>\n"
        else:
            nav_html += "<div></div>\n"
        
        if next_num:
            next_file = lecture_map[next_num]
            nav_html += f"<div>\n[Next: Lecture {next_num} →]({next_file})\n</div>\n"
        else:
            nav_html += "<div></div>\n"
        
        nav_html += ":::\n"
        
        # Check if content ends with :::
        if content.rstrip().endswith(":::"):
            # Add navigation after the last closing :::
            last_index = content.rstrip().rfind(":::")
            new_content = content[:last_index+3] + nav_html
        else:
            # Just append the navigation
            new_content = content + nav_html
        
        # Write the updated content
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(new_content)
        
        print(f"  Added navigation to {filename}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)  # Change to the script directory
    add_navigation_to_lectures()
    print("Navigation added to all lecture files.")
