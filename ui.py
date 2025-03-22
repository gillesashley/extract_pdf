def display_menu():
    """
    Display the main menu options to the user.
    """
    print("\n===== PDF Processing Tool =====")
    print("1. Extract pages from a PDF")
    print("2. Merge multiple PDFs in chunks")
    print("3. Quit")
    print("=============================")


def get_user_choice():
    """
    Get and validate the user's menu choice.
    
    Returns:
        int: The validated user choice (1, 2, or 3)
    """
    while True:
        try:
            choice = int(input("\nEnter your choice (1-3): "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_extraction_params():
    """
    Get parameters for PDF page extraction from user input.
    
    Returns:
        tuple: (input_path, output_path, start_page, end_page)
    """
    input_path = input("Enter the input PDF file path: ")
    output_path = input("Enter the output PDF file path: ")
    
    while True:
        try:
            start_page = int(input("Enter the start page number: "))
            if start_page < 1:
                print("Start page must be at least 1.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    while True:
        try:
            end_page = int(input("Enter the end page number: "))
            if end_page < start_page:
                print("End page must be greater than or equal to start page.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    return input_path, output_path, start_page, end_page


def get_merge_params():
    """
    Get parameters for PDF merging from user input.
    
    Returns:
        tuple: (input_dir, output_dir, chunk_size)
    """
    input_dir = input("Enter the directory containing PDF files to merge: ")
    output_dir = input("Enter the output directory for merged files: ")
    
    while True:
        try:
            chunk_size = int(input("Enter the number of PDFs to merge into each output file: "))
            if chunk_size < 1:
                print("Chunk size must be at least 1.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    return input_dir, output_dir, chunk_size