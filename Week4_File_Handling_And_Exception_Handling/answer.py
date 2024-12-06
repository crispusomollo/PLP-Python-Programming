def modify_file_content(input_filename, output_filename):
    """
    Reads a file, modifies its content, and writes it to a new file.

    Args:
        input_filename (str): Name of the file to read.
        output_filename (str): Name of the file to write the modified content.
    """
    try:
        # Attempt to open and read the input file
        with open(input_filename, "r") as infile:
            content = infile.readlines()

        # Modify the content: Example - prepend line numbers
        modified_content = [f"{i + 1}: {line}" for i, line in enumerate(content)]

        # Write the modified content to the output file
        with open(output_filename, "w") as outfile:
            outfile.writelines(modified_content)

        print(f"Modified content written to '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main program
if __name__ == "__main__":
    # Ask the user for the input and output file names
    input_file = input("Enter the name of the file to read: ")
    output_file = input("Enter the name of the file to write the modified content: ")

    # Call the function
    modify_file_content(input_file, output_file)
