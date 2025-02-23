import fitz  # PyMuPDF
import os

def merge_pdfs(pdf_folder, output_filename):
    pdf_writer = fitz.open()
    
    # Get all PDF files in the folder
    pdf_files = sorted([f for f in os.listdir(pdf_folder) if f.endswith(".pdf")])
    
    if not pdf_files:
        print("No PDF files found in the folder.")
        return
    
    print("Merging the following files:")
    for pdf_file in pdf_files:
        print(pdf_file)
        pdf_reader = fitz.open(os.path.join(pdf_folder, pdf_file))
        pdf_writer.insert_pdf(pdf_reader)
    
    # Save the merged PDF
    output_path = os.path.join(pdf_folder, output_filename)
    pdf_writer.save(output_path)
    pdf_writer.close()
    print(f"Merged PDF saved as: {output_path}")

if __name__ == "__main__":
    folder_path = input("Enter the folder containing PDF files: ")
    output_file = input("Enter the name of the output PDF file: ")
    merge_pdfs(folder_path, output_file)
