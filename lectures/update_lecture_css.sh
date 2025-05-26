#!/bin/bash
# Script to update CSS in all lecture pages to include dark-mode.css

echo "Updating CSS in all lecture files..."
cd /home/kmcalist/ClassSites/QTM447/lectures

for file in lecture*.qmd; do
  echo "Processing $file..."
  
  # Check if file already includes dark-mode.css
  if grep -q "dark-mode.css" "$file"; then
    echo "  $file already has dark-mode.css"
  else
    # Replace the CSS line with multiple CSS
    sed -i 's/css: \.\.\\/styles\.css/css: \n      - \.\.\\/styles\.css\n      - \.\.\\/dark-mode\.css/' "$file"
    echo "  Updated CSS in $file"
  fi
done

echo "CSS updated in all lecture files."
