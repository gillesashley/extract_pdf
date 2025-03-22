# Import functions from the pdf_operations module
from pdf_operations import extract_pdf_pages, merge_pdf_files, scan_and_merge_pdfs

# Import functions from the ui module
from ui import display_menu, get_user_choice, get_extraction_params, get_merge_params


# Main program
def main():
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == 1:  # Extract pages from a PDF
            print("\n--- Extract Pages from PDF ---")
            input_path, output_path, start_page, end_page = get_extraction_params()
            extract_pdf_pages(input_path, output_path, start_page, end_page)
            
        elif choice == 2:  # Merge PDFs in chunks
            print("\n--- Merge PDFs in Chunks ---")
            input_dir, output_dir, chunk_size = get_merge_params()
            scan_and_merge_pdfs(input_dir, output_dir, chunk_size)
            
        elif choice == 3:  # Quit
            print("\nThank you for using the PDF Processing Tool. Goodbye!")
            break


if __name__ == "__main__":
    main()
