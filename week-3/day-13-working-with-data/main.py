# Day 13 — Working With Data
# Task: Load a CSV, manipulate lists and dicts, clean data, and print a summary.
# Submit this script along with your original CSV and the output CSV.

import csv
import os

# Build the file paths from this script's own folder, so the program
# works no matter which folder the terminal is in when you run it
BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(BASE_FOLDER, "data", "sample.csv")
OUTPUT_FILE = os.path.join(BASE_FOLDER, "data", "output.csv")


# Step 1: Load CSV
# Open the CSV file using csv.DictReader and read each row into a list of dicts.

def load_data(filepath):
    rows = []
    # Open the file and read rows into the list
    with open(filepath, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Clean the text fields: remove extra spaces and standardise the case
            row["NAME"] = row["NAME"].strip().title()
            row["DEPARTMENT"] = row["DEPARTMENT"].strip().upper()

            # Convert the score from a string to an integer
            row["SCORE"] = int(row["SCORE"])

            rows.append(row)
    return rows


# Step 2: Print Summary
# Print the total number of rows.
# For any numeric column, print the minimum, maximum, and average values.

def print_summary(rows):
    # Collect all the scores into a list
    scores = []
    for row in rows:
        scores.append(row["SCORE"])

    print("Data Summary")
    print("Total rows:", len(rows))
    print("Lowest score:", min(scores))
    print("Highest score:", max(scores))
    print("Average score:", round(sum(scores) / len(scores), 2))


# Step 3: Filter Data
# Return only the rows where a specific column meets a condition.
# Example: score above 70, or price below 50.

def filter_data(rows):
    filtered = []
    # Keep only the students who scored 70 and above (Grade A)
    for row in rows:
        if row["SCORE"] >= 70:
            filtered.append(row)
    return filtered


# Step 4: Sort and Export
# Sort the filtered data by one column and write the result to OUTPUT_FILE.

# sort() needs to know which value to sort by, since each row is a dictionary.
# This small function returns the score of one row, and we pass it using key=
def get_score(row):
    return row["SCORE"]


def save_data(rows, filepath):
    # Sort rows by score, highest first, then write to CSV
    rows.sort(key=get_score, reverse=True)

    fieldnames = ["NAME", "DEPARTMENT", "SCORE"]

    with open(filepath, "w", newline="") as new_file:
        writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


# Main
def main():
    rows = load_data(INPUT_FILE)
    print_summary(rows)
    filtered = filter_data(rows)
    save_data(filtered, OUTPUT_FILE)
    print(f"Done. {len(filtered)} rows written to data/output.csv")


if __name__ == "__main__":
    main() 