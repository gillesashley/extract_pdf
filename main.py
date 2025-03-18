from PyPDF2 import PdfReader, PdfWriter


def extract_pdf_pages(input_path, output_path, start_page, end_page):
    """
    Extract a range of pages from a PDF file and save them to a new PDF.

    Args:
        input_path (str): Path to the input PDF file
        output_path (str): Path where the output PDF will be saved
        start_page (int): First page to extract (1-based indexing)
        end_page (int): Last page to extract (1-based indexing)
    """
    try:
        # Create PDF reader object
        reader = PdfReader(input_path)

        # Create PDF writer object
        writer = PdfWriter()

        # Convert to 0-based indexing
        start_idx = start_page - 1
        end_idx = end_page - 1

        # Validate page range
        if start_idx < 0 or end_idx >= len(reader.pages):
            raise ValueError("Page range is out of bounds")

        # Add selected pages to writer
        for page_num in range(start_idx, end_idx + 1):
            writer.add_page(reader.pages[page_num])

        # Write the output PDF file
        with open(output_path, "wb") as output_file:
            writer.write(output_file)

        print(f"Successfully extracted pages {start_page}-{end_page} to {output_path}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Example usage
input_file = "Week 7 Nov 2024st.pdf"
output_file = "Week 7 Nov 2024st_extracted.pdf"
start_page = 1
end_page = 60

extract_pdf_pages(input_file, output_file, start_page, end_page)
