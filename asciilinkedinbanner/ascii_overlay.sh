#!/bin/bash

# Set the text you want to display
TEXT="BuildSomething!"
FONT="slant"
WIDTH=80  # Adjust width as needed
HEIGHT=10 # Adjust height as needed

# Generate Figlet text
FIGLET_TEXT=$(figlet -f $FONT "$TEXT")

# Generate a random background of 1s and 0s
BACKGROUND=""
for ((i = 0; i < HEIGHT; i++)); do
    BACKGROUND+=$(cat /dev/urandom | tr -dc '01' | fold -w $WIDTH | head -n 1)
    BACKGROUND+="\n"
done

# Merge Figlet text with background
echo -e "$BACKGROUND" | awk -v figlet="$FIGLET_TEXT" '
BEGIN { split(figlet, lines, "\n"); lineNum=1 }
{
    if (lineNum in lines) {
        print substr($0, 1, 20) lines[lineNum] substr($0, 20 + length(lines[lineNum]))
        lineNum++
    } else {
        print
    }
}
'
