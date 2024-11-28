import PyPDF2

def extract_pages():
    # Prompt user for input PDF file
    input_file = input("Enter the name of the PDF file in the same directory (e.g., input.pdf): ")

    # Prompt user for the range of pages to extract
    try:
        start_page = int(input("Enter the page number to start extraction (1-based index): "))
        end_page = int(input("Enter the page number to end extraction (inclusive): "))
    except ValueError:
        print("Invalid input. Please enter numeric values for page numbers.")
        return

    # Prompt user for the output PDF file name
    output_file = input("Enter the name for the new PDF file (e.g., output.pdf): ")

    try:
        # Open the input PDF file
        with open(input_file, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            
            # Validate page range
            total_pages = len(reader.pages)
            if start_page < 1 or end_page > total_pages or start_page > end_page:
                print(f"Invalid page range. The PDF has {total_pages} pages.")
                return
            
            # Create a PDF writer object
            writer = PyPDF2.PdfWriter()
            
            # Add the specified pages to the writer
            for page_num in range(start_page - 1, end_page):
                writer.add_page(reader.pages[page_num])
            
            # Write the new PDF file
            with open(output_file, 'wb') as new_pdf:
                writer.write(new_pdf)
            
            print(f"Pages {start_page} to {end_page} have been successfully extracted to {output_file}.")
    except FileNotFoundError:
        print("The specified file was not found. Please check the file name and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the program
if __name__ == "__main__":
    extract_pages()
