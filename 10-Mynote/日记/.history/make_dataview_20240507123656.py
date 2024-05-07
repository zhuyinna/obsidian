import os
from collections import defaultdict

def generate_markdown_file(directory):
    # Dictionary to store notes by month
    notes_by_month = defaultdict(list)

    # Iterate through directory and subdirectories to find markdown files
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                # Extract the date from the file name
                date = file[:10]
                # Group notes by month
                month = date[:7]
                notes_by_month[month].append("[[" + date + "]]")
                print(f"Found note: {date}")

# Generate markdown content
markdown_content = "|         | 1              | 2   | 3   | 4   | 5   | 6   | 7   |\n"
markdown_content += "| ------- | -------------- | --- | --- | --- | --- | --- | --- |\n"
current_column = 0

for month, notes in sorted(notes_by_month.items()):
    if current_column == 0:
        markdown_content += f"| {month} | {' | '.join(notes)} |"
        current_column += 1
    elif current_column == 6:
        markdown_content += f" {' | '.join(notes)} |\n"
        current_column = 0
    else:
        markdown_content += f" {' | '.join(notes)} |"
        current_column += 1

# Specify the directory containing the markdown files
directory = "."
generate_markdown_file(directory)
