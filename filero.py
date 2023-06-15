filepath = input("Enter the file path: ")

try:
    # Open the file
    with open(filepath, 'r') as file:
        # Read the file contents
        contents = file.read()

        # Count the number of lines
        line_count = contents.count('\n') + 1

        # Count the number of words
        word_count = len(contents.split())

    # Display the results
    print("Number of lines:", line_count)
    print("Number of words:", word_count)

except FileNotFoundError:
    print("File not found!")