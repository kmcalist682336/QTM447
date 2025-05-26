#!/bin/bash
# Script to render the QTM447 site with improved styling and no dark mode

echo "Rendering QTM447 website..."
cd /home/kmcalist/ClassSites/QTM447

# Remove dark mode files (optional - we can keep them for reference)
# echo "Removing dark mode files..."
# rm -f dark-mode*.css dark-mode*.js

# Clean the _site directory first
if [ -d "_site" ]; then
  echo "Cleaning _site directory..."
  rm -rf _site/*
fi

# Render with Quarto
echo "Running quarto render..."
quarto render

echo "Site rendered successfully!"
echo "You can now view the site by serving it from the _site directory:"
echo "  cd _site && python -m http.server 8000"
echo "Then visit http://localhost:8000 in your browser."
