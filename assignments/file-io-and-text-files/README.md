# 📘 Assignment: File I/O and Working with Text Files

## 🎯 Objective

Learn how to read, write, and process files in Python. You'll work with text files, handle file operations safely, and develop skills for data persistence that are essential for real-world applications.

## 📝 Tasks

### 🛠️ Reading and Writing Files

#### Description
Create functions to read from files and write data to new files using Python's file handling operations.

#### Requirements
Completed program should:

- Open and read a file line by line using a `for` loop or the `readlines()` method.
- Count the number of lines in a file.
- Write a list of strings to a new file (one per line).
- Use proper file handling with `open()` and ensure files are closed (use context managers with `with`).
- Example:
  ```python
  read_file('input.txt')  # Prints each line
  write_file('output.txt', ['Line 1', 'Line 2', 'Line 3'])
  ```

### 🛠️ Processing and Transforming File Data

#### Description
Read data from a file, process it (transform, filter, or analyze), and write results to a new file.

#### Requirements
Completed program should:

- Read a text file containing a list of items (one per line).
- Filter or transform the data (e.g., remove blanks, convert to uppercase, sort alphabetically).
- Write the processed data to a new output file.
- Display statistics (e.g., original count vs. filtered count).
- Example: Read a list of names, remove duplicates, sort them, and save to `unique_sorted_names.txt`.

### 🛠️ Error Handling and File Management

#### Description
Implement robust file handling with error management for real-world scenarios.

#### Requirements
Completed program should:

- Handle the case when a file doesn't exist (catch `FileNotFoundError`).
- Handle permission errors gracefully.
- Ask the user for a filename and read it safely.
- Provide meaningful error messages to the user.
- Use context managers (`with` statement) for all file operations to ensure proper cleanup.
- Example error handling:
  ```python
  try:
      with open(filename, 'r') as f:
          content = f.read()
  except FileNotFoundError:
      print(f"Error: File '{filename}' not found.")
  ```
