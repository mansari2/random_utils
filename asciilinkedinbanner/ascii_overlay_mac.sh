#!/bin/bash

# Set text and font
TEXT="BuildSomething!"
FONT="slant"
WIDTH=80   # Width of the background
HEIGHT=15  # Number of lines in the background
OUTPUT_FILE="output.txt"

# Generate Figlet text and store in a temporary file
FIGLET_FILE=$(mktemp)
figlet -f "$FONT" "$TEXT" > "$FIGLET_FILE"

# Generate background of 1s and 0s
{
    for ((i = 0; i < HEIGHT; i++)); do
        cat /dev/urandom | LC_CTYPE=C tr -dc '01' | fold -w "$WIDTH" | head -n 1
    done
} | awk -v figlet_file="$FIGLET_FILE" '
BEGIN {
    while ((getline line < figlet_file) > 0) {
        figlet_lines[NR] = line;
    }
    close(figlet_file);
}
{
    line_number++;
    if (line_number in figlet_lines) {
        left_padding = int(0.3 * length($0)); # Adjust text centering
        print substr($0, 1, left_padding) figlet_lines[line_number] substr($0, left_padding + length(figlet_lines[line_number]) + 1);
    } else {
        print;
    }
}' | tee "$OUTPUT_FILE"

# Cleanup temporary file
rm "$FIGLET_FILE"

echo "Output saved to $OUTPUT_FILE"

