#!/usr/bin/env python3
import os
import glob
import subprocess
import sys
import re

def convert_notebooks_to_html():
    """Convert .ipynb files to .html in both slideipynb and ipynbs directories"""
    
    # Paths to notebook directories
    slide_ipynb_dir = "slideipynb"
    lecture_ipynb_dir = "ipynbs"
    
    # Create HTML output directories if they don't exist
    slide_html_dir = "slideipynb_html"
    lecture_html_dir = "ipynbs_html"
    
    os.makedirs(slide_html_dir, exist_ok=True)
    os.makedirs(lecture_html_dir, exist_ok=True)
    
    # Process slide notebooks
    print("Converting slide notebooks to HTML...")
    slide_notebooks = glob.glob(f"{slide_ipynb_dir}/Lecture*.ipynb")
    for nb_path in slide_notebooks:
        try:
            base_name = os.path.basename(nb_path)
            name_no_ext = os.path.splitext(base_name)[0]
            html_path = f"{slide_html_dir}/{name_no_ext}.html"
            
            print(f"Converting {nb_path} to {html_path}")
            cmd = f"jupyter nbconvert --to html {nb_path} --output-dir {slide_html_dir}"
            subprocess.run(cmd, shell=True, check=True)
        except Exception as e:
            print(f"Error converting {nb_path}: {e}")
    
    # Process lecture code notebooks
    print("\nConverting lecture code notebooks to HTML...")
    lecture_notebooks = glob.glob(f"{lecture_ipynb_dir}/Lecture*Code.ipynb")
    for nb_path in lecture_notebooks:
        try:
            base_name = os.path.basename(nb_path)
            name_no_ext = os.path.splitext(base_name)[0]
            html_path = f"{lecture_html_dir}/{name_no_ext}.html"
            
            print(f"Converting {nb_path} to {html_path}")
            cmd = f"jupyter nbconvert --to html {nb_path} --output-dir {lecture_html_dir}"
            subprocess.run(cmd, shell=True, check=True)
        except Exception as e:
            print(f"Error converting {nb_path}: {e}")
    
    print("\nConversion complete!")
    print(f"HTML files for slides are in: {slide_html_dir}")
    print(f"HTML files for lecture code are in: {lecture_html_dir}")

def update_lecture_pages():
    """Update all lecture pages to point to HTML versions of notebooks instead of .ipynb"""
    print("\nUpdating lecture pages to point to HTML versions...")
    
    lecture_pages = glob.glob("lecture*.qmd")
    updates_count = 0
    
    for page_path in sorted(lecture_pages):
        try:
            with open(page_path, 'r') as f:
                content = f.read()
            
            # Replace slide code links
            updated_content = re.sub(
                r'<a href="slideipynb/Lecture(\d+).ipynb"',
                r'<a href="slideipynb_html/Lecture\1.html"',
                content
            )
            
            # Replace lecture code links
            updated_content = re.sub(
                r'<a href="ipynbs/Lecture(\d+)Code.ipynb"',
                r'<a href="ipynbs_html/Lecture\1Code.html"',
                updated_content
            )
            
            if updated_content != content:
                with open(page_path, 'w') as f:
                    f.write(updated_content)
                lecture_num = re.search(r'lecture(\d+).qmd', page_path).group(1)
                print(f"Updated {page_path}")
                updates_count += 1
        
        except Exception as e:
            print(f"Error updating {page_path}: {e}")
    
    print(f"\nUpdated {updates_count} lecture pages.")

if __name__ == "__main__":
    print("Starting notebook to HTML conversion...")
    convert_notebooks_to_html()
    update_lecture_pages()
