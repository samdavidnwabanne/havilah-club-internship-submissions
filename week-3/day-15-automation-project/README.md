# Day 15 — Python Automation Project

## What does this project do?

This project is a file organiser. It scans the `data/` folder, looks at the extension of every file, and moves each file into a subfolder named after that extension inside `data/output/`. For example, `notes.txt` goes into `txt_files/` and `photo.jpg` goes into `jpg_files/`. It saves the time of sorting a messy folder by hand, and it prints a summary of how many files went into each folder.

## Project Type

File Organiser (Option A)

## Requirements

No extra libraries are needed. The project only uses `os` and `shutil`, which are part of the Python standard library, so there is nothing to install.

## How to run

```bash
python main.py
```

The program finds the `data/` folder from its own location, so it also works when run from another folder, for example `python week-3/day-15-automation-project/main.py` from the repository root.

The files are moved, not copied. After one run the sample files are inside `data/output/`. To run it again, put the sample files back in `data/`.

## Example output

Running the script on the nine sample files in `data/`:

```
Starting automation...
Moved README_old to no_extension/
Moved budget.xlsx to xlsx_files/
Moved data.csv to csv_files/
Moved notes.txt to txt_files/
Moved photo.jpg to jpg_files/
Moved report.pdf to pdf_files/
Moved script.py to py_files/
Moved song.mp3 to mp3_files/
Moved todo.txt to txt_files/

Summary
no_extension: 1 file(s)
xlsx_files: 1 file(s)
csv_files: 1 file(s)
txt_files: 2 file(s)
jpg_files: 1 file(s)
pdf_files: 1 file(s)
py_files: 1 file(s)
mp3_files: 1 file(s)
Total files moved: 9
Done.
```

## Automation plan

Input: the files inside the `data/` folder (nine sample files with different extensions).

Process:
1. Check that the input folder exists and is really a folder
2. List the files, skipping subfolders and hidden files
3. Work out the folder name from each file's extension
4. Create the destination folder inside `data/output/` if it does not exist
5. Move the file and count it

Output: one message per file moved, then a summary with the number of files in each new folder and the total.

Edge cases handled:
- The input folder does not exist, or the path is a file instead of a folder: an error message is shown and the program stops safely
- The folder has no files: the program says there is nothing to organise
- A file has no extension: it goes into `no_extension/`
- A file with the same name is already in the destination folder: it is skipped, so nothing is overwritten
- A file cannot be moved, for example because of a permission problem: `try` / `except OSError` skips it and continues
- Hidden files such as `.gitkeep` are ignored

## Functions

| Function | What it does |
|---|---|
| `get_folder_name(filename)` | returns the destination folder name for a file |
| `get_files(folder_path)` | lists only the files in a folder |
| `move_file(input_path, output_path, filename)` | creates the folder and moves one file |
| `print_summary(counts)` | prints the final summary |
| `process(input_path, output_path)` | runs the whole automation and handles the edge cases |

## Tests performed

| Test | Result |
|---|---|
| Normal run with 9 files and 8 different folders | all files moved, summary correct |
| Run again after everything was moved | "The folder has no files to organise." |
| Folder that does not exist | error message, no crash |
| Path that is a file, not a folder | error message, no crash |
| Duplicate filename already in the destination | file skipped, original kept |
| Hidden file `.gitkeep` in the folder | left in place |