def modify_content(content):
    return content.upper()

def main():
    # Ask user for filename
    filename = input("Enter the filename to read: ")

    try:
        # Read the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify content
        modified_content = modify_content(content)

        # Write modified content to new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to {new_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You don't have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
