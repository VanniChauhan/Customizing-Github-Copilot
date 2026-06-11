def read_file(filename):
    """
    TODO: Read a file and print its contents line by line.
    
    Args:
        filename (str): The name of the file to read
    
    Returns:
        None (prints to console)
    
    Example:
        read_file('input.txt')
    """
    pass


def write_file(filename, lines):
    """
    TODO: Write a list of strings to a file (one line per string).
    
    Args:
        filename (str): The name of the file to write to
        lines (list): A list of strings to write
    
    Returns:
        None (writes to file)
    
    Example:
        write_file('output.txt', ['Hello', 'World', 'Python'])
    """
    pass


def count_lines(filename):
    """
    TODO: Count the number of lines in a file.
    
    Args:
        filename (str): The name of the file to count
    
    Returns:
        int: The number of lines in the file
    
    Example:
        lines = count_lines('input.txt')
        print(f"The file has {lines} lines")
    """
    pass


def process_file(input_filename, output_filename, transform_func):
    """
    TODO: Read from input_filename, apply transform_func to each line,
    and write results to output_filename.
    
    Args:
        input_filename (str): The input file to read from
        output_filename (str): The output file to write to
        transform_func (function): A function that takes a line and returns processed line
    
    Returns:
        None (writes to file)
    
    Example:
        process_file('names.txt', 'uppercase_names.txt', str.upper)
    """
    pass


def read_file_safe(filename):
    """
    TODO: Read a file with error handling for FileNotFoundError and other exceptions.
    
    Args:
        filename (str): The name of the file to read
    
    Returns:
        str: The file contents, or an error message if file cannot be read
    
    Example:
        content = read_file_safe('missing.txt')
    """
    pass


# TODO: Test your functions
if __name__ == "__main__":
    # Example 1: Write a file
    # write_file('sample.txt', ['Python', 'Programming', 'Is', 'Fun'])
    
    # Example 2: Read the file
    # read_file('sample.txt')
    
    # Example 3: Count lines
    # line_count = count_lines('sample.txt')
    # print(f"Total lines: {line_count}")
    
    # Example 4: Process and transform
    # process_file('sample.txt', 'uppercase.txt', str.upper)
    
    # Example 5: Safe read with error handling
    # content = read_file_safe('nonexistent.txt')
    pass
