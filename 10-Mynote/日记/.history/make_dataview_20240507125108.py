import os
from collections import defaultdict

NUM_PER_ROW = 5
def generate_markdown_file(directory):
    # Dictionary to store notes by month
    notes_by_month = defaultdict(list)

    # Iterate through directory and subdirectories to find markdown files
    for root, _, files in os.walk(directory):
        for file in files:
            # 如果file不是以日期格式的文件，则跳过：
            if len(file) < 10 or not file[:10].isdigit():
            if file.endswith(".md"):
                # Extract the date from the file name
                date = file[:10]
                # Group notes by month
                month = file[:7]
                notes_by_month[month].append("[[" + date + "]]")
                print(f"Found note: {date}")

    # Generate markdown content
    markdown_content = "| |1|2|3|4|5|\n"
    markdown_content += "| -- | -- | -- | -- | -- | -- |\n"

    for month, notes in sorted(notes_by_month.items()):
        notes_chunked = [notes[i:i+NUM_PER_ROW] for i in range(0, len(notes), NUM_PER_ROW)]  # Split notes into chunks of 7
        for chunk in notes_chunked:
            markdown_content += f"| {month} | {' | '.join(chunk)} {' | ' * (NUM_PER_ROW-len(chunk))} |\n"
    # Write markdown content to file
    with open("output.md", "w") as f:
        f.write(markdown_content)

# Specify the directory containing the markdown files
directory = "."
generate_markdown_file(directory)
