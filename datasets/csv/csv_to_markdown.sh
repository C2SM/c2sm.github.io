#!/bin/bash

# Loop through all CSV files in the current directory
for csv_file in *.csv; do
    # Extract the file name without extension
    base_name=$(basename "$csv_file" .csv)
    
    # Define the output Markdown file name
    markdown_file="$base_name.md"
    
    # Perform CSV to Markdown conversion using sed
    sed -e 's/","/ | /g' -e 's/^"/| /' -e 's/"$//' -e 's/^$/| | | | | | | | | | |/' "$csv_file" > "$markdown_file"
    
    # Print a message indicating the conversion is complete
    echo "CSV file '$csv_file' converted to '$markdown_file'."
done

echo "Conversion complete."

