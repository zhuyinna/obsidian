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

    # Generate markdown content
    markdown_content = ""
    for i, (month, notes) in enumerate(sorted(notes_by_month.items())):
        if i==0: 
            markdown_content += f"|         | 1              | 2   | 3   | 4   | 5   | 6   | 7   |\n"
            markdown_content += f"| ------- | -------------- | --- | --- | --- | --- | --- | --- |\n"
            markdown_content += f"| {month} | {' | '.join(notes)} |     |     |     |     |     |     |\n"
            markdown_content += f"|         |                |     |     |     |     |     |     |\n"
            markdown_content += f"|         |                |     |     |     |     |     |     |\n\n"

    # Write markdown content to file
    with open("output.md", "w") as f:
        f.write(markdown_content)

# Specify the directory containing the markdown files
directory = "10-Mynote"
generate_markdown_file(directory)
