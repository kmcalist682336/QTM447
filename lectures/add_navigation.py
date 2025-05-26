#!/usr/bin/env python3
import os
import re
import glob

def add_navigation_to_lectures():
    """Add navigation links to lecture pages"""
    
    lecture_files = sorted(glob.glob("lecture*.qmd"))
    total_lectures = len(lecture_files)
    
    for i, file_path in enumerate(lecture_files):
        # Extract lecture number
        match = re.search(r'lecture(\d+)\.qmd', file_path)
        if not match:
            continue
        
        current_num = int(match.group(1))
        
        # Create navigation HTML
        nav_html = '\n\n::: {.lecture-nav style="display: flex; justify-content: space-between; margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #ddd;"}\n'
        
        # Previous lecture link
        if current_num > 1:
            prev_num = current_num - 1
            nav_html += f'<div>\n[← Previous: Lecture {prev_num}](lecture{prev_num}.qmd)\n</div>\n'
        else:
            nav_html += '<div></div>\n'
        
        # Next lecture link
        if current_num < total_lectures:
            next_num = current_num + 1
            nav_html += f'<div>\n[Next: Lecture {next_num} →](lecture{next_num}.qmd)\n</div>\n'
        else:
            nav_html += '<div></div>\n'
        
        nav_html += ':::\n'
        
        # Read the file content
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Check if navigation already exists
        if '::: {.lecture-nav' in content:
            print(f"Navigation already exists in {file_path}, skipping...")
            continue
        
        # Find where to insert navigation (before the last :::)
        last_close_tag = content.rfind(':::')
        if last_close_tag > 0:
            updated_content = content[:last_close_tag] + nav_html + content[last_close_tag:]
            
            # Write the updated content back
            with open(file_path, 'w') as f:
                f.write(updated_content)
            
            print(f"Added navigation to {file_path}")
        else:
            print(f"Could not find insertion point in {file_path}")

if __name__ == "__main__":
    print("Adding navigation to lecture pages...")
    add_navigation_to_lectures()
    print("Done!")
