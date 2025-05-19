def read_and_modify_file():
    # Ask user for the input filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Try to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
            print("File read successfully.")

        # Modify content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Create output filename
        new_filename = "modified_" + filename

        # Write modified content to a new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
            print(f"Modified content written to '{new_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read or write to '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_and_modify_file()