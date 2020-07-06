# extract pages from a PDF
# Pre-Requisites - PyPDF2 (pip install PyPDF2)

from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_file_path = 'AWS.pdf' # file from which you want
file_base_Name = pdf_file_path.replace('.pdf', '')

pdf = PdfFileReader(pdf_file_path)

pages = [15,16,17] # select pages you want to extract
pdfWriter = PdfFileWriter()

for page_num in pages:
    pdfWriter.addPage(pdf.getPage(page_num))
    
    with open('{0}_extract.pdf'.format(file_base_Name), 'wb') as f: # exports filename with _extract.pdf appended
        pdfWriter.write(f)
        f.close()
