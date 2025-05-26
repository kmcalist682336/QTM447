#!/bin/bash
# Script to update CSS in all lecture pages to remove dark-mode.css

echo "Updating CSS in all lecture files..."
cd /home/kmcalist/ClassSites/QTM447/lectures

for file in lecture*.qmd; do
  echo "Processing $file..."
  
  # Check if file includes dark-mode.css
  if grep -q "dark-mode.css" "$file"; then
    # Replace the multiple CSS with single CSS
    sed -i 's/css: \n      - \.\.\\/styles\.css\n      - \.\.\\/dark-mode\.css/css: \.\.\\/styles\.css/' "$file"
    echo "  Removed dark-mode.css from $file"
  fi
done

echo "CSS updated in all lecture files."
