# Day 15 — Python Automation Project
# Choose one project type and implement it here:
#
#   A) File Organiser  — scans a folder and moves files into subfolders by extension
#   B) Report Generator — reads a CSV and produces a formatted text summary
#   C) Data Cleaner    — removes duplicate rows, strips whitespace, standardises columns
#
# Submit the complete project (this file + data folder + README.md) to GitHub.

import os
import shutil


# Configuration
# Set your input/output paths here so they are easy to find and change.

# Build the paths from this script's own folder, so the program
# works no matter which folder the terminal is in when you run it
BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(BASE_FOLDER, "data")
OUTPUT_PATH = os.path.join(BASE_FOLDER, "data", "output")


# Core Functions
# Break your project into small, clearly named functions.
# Each function should do one thing.

def get_folder_name(filename):
    # splitext splits "notes.txt" into ("notes", ".txt")
    extension = os.path.splitext(filename)[1].lower()

    # Edge case: a file with no extension
    if extension == "":
        return "no_extension"

    # ".txt" becomes "txt_files" (extension[1:] removes the dot)
    return extension[1:] + "_files"


def get_files(folder_path):
    files = []

    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)

        # Skip subfolders (like output) and hidden files (like .gitkeep)
        if os.path.isfile(full_path) and not item.startswith("."):
            files.append(item)

    files.sort()
    return files


def move_file(input_path, output_path, filename):
    folder_name = get_folder_name(filename)
    destination_folder = os.path.join(output_path, folder_name)

    # exist_ok=True means "don't crash if the folder already exists"
    os.makedirs(destination_folder, exist_ok=True)

    source_path = os.path.join(input_path, filename)
    destination_path = os.path.join(destination_folder, filename)

    # Edge case: a file with the same name is already in the destination
    if os.path.exists(destination_path):
        print(f"Skipped {filename}: a file with this name is already in {folder_name}/")
        return None

    shutil.move(source_path, destination_path)
    print(f"Moved {filename} to {folder_name}/")
    return folder_name


def print_summary(counts):
    total = 0

    print("\nSummary")
    for folder_name in counts:
        print(f"{folder_name}: {counts[folder_name]} file(s)")
        total = total + counts[folder_name]

    print(f"Total files moved: {total}")


def process(input_path, output_path):
    # Edge case: the folder does not exist
    if not os.path.exists(input_path):
        print(f"Error: the folder '{input_path}' does not exist.")
        return

    # Edge case: the path points to a file, not a folder
    if not os.path.isdir(input_path):
        print(f"Error: '{input_path}' is not a folder.")
        return

    files = get_files(input_path)

    # Edge case: nothing to organise
    if len(files) == 0:
        print("The folder has no files to organise.")
        return

    counts = {}    # keeps track of how many files went into each folder

    for filename in files:
        try:
            folder_name = move_file(input_path, output_path, filename)
        except OSError:
            # For example, a file that is locked or has no permission
            print(f"Could not move {filename}. Skipping it.")
            continue

        if folder_name is not None:
            if folder_name in counts:
                counts[folder_name] = counts[folder_name] + 1
            else:
                counts[folder_name] = 1

    print_summary(counts)


# Main
def main():
    print("Starting automation...")
    process(INPUT_PATH, OUTPUT_PATH)
    print("Done.")


if __name__ == "__main__":
    main() 