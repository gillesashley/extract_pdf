import os
import re
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


def merge_pdf_files(input_files, output_path):
    """
    Merge multiple PDF files into a single PDF file.

    Args:
        input_files (list): List of paths to the input PDF files
        output_path (str): Path where the output merged PDF will be saved
    """
    try:
        # Create PDF writer object
        writer = PdfWriter()

        # Add all pages from each PDF file
        for input_file in input_files:
            try:
                reader = PdfReader(input_file)
                for page in reader.pages:
                    writer.add_page(page)
                print(f"Added {len(reader.pages)} pages from {os.path.basename(input_file)}")
            except Exception as e:
                print(f"Error processing {input_file}: {str(e)}")
                continue

        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Write the output PDF file
        with open(output_path, "wb") as output_file:
            writer.write(output_file)

        print(f"Successfully merged {len(input_files)} PDF files to {output_path}")
        return True

    except Exception as e:
        print(f"An error occurred during merging: {str(e)}")
        return False


def scan_and_merge_pdfs(input_dir, output_dir, chunk_size=5):
    """
    Scan a directory for PDF files and merge them in chunks.

    Args:
        input_dir (str): Directory containing PDF files to merge
        output_dir (str): Directory where merged PDF files will be saved
        chunk_size (int): Number of PDF files to merge into each output file
    """
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Get all PDF files in the directory
        pdf_files = []
        for file in os.listdir(input_dir):
            if file.lower().endswith(".pdf"):
                pdf_files.append(os.path.join(input_dir, file))

        if not pdf_files:
            print(f"No PDF files found in {input_dir}")
            return

        # Sort files alphabetically
        pdf_files.sort()

        # Group files into chunks
        chunks = [pdf_files[i:i + chunk_size] for i in range(0, len(pdf_files), chunk_size)]

        # Merge each chunk
        for i, chunk in enumerate(chunks):
            # Create a descriptive name for the merged file
            if len(chunk) == 1:
                # If there's only one file in the chunk, use its basename
                base_name = os.path.splitext(os.path.basename(chunk[0]))[0]
                output_name = f"{base_name}_merged.pdf"
            else:
                # Use the first and last file names to create a descriptive name
                first_file = os.path.splitext(os.path.basename(chunk[0]))[0]
                last_file = os.path.splitext(os.path.basename(chunk[-1]))[0]
                
                # Clean up filenames to make them suitable for file naming
                first_file = re.sub(r'[^\w\s-]', '', first_file)[:20]  # Take first 20 chars
                last_file = re.sub(r'[^\w\s-]', '', last_file)[:20]  # Take first 20 chars
                
                output_name = f"merged_{i+1:03d}_{first_file}_to_{last_file}.pdf"

            output_path = os.path.join(output_dir, output_name)
            
            # Merge the chunk
            print(f"Merging chunk {i+1}/{len(chunks)} ({len(chunk)} files)...")
            merge_pdf_files(chunk, output_path)

        print(f"Merged {len(pdf_files)} PDF files into {len(chunks)} output files in {output_dir}")

    except Exception as e:
        print(f"An error occurred during scanning and merging: {str(e)}")