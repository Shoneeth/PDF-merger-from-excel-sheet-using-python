import PyPDF2
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from io import BytesIO
from PyPDF2 import PdfReader,PdfMerger

def merge_pdf_from_drive_links(drive_links, output_filename):
    # Set up authentication using the PyDrive library
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()  # Opens a new tab to authenticate
    drive = GoogleDrive(gauth)

    # Loop through the Google Drive links and download the PDF files
    pdf_files = []
    for link in drive_links:
        #pdf_files = []
        file_id = link.split('/')[-2]
        file = drive.CreateFile({'id': file_id})
        file.GetContentFile(file_id)
        pdf_files.append(file_id)
        #pdf_merger = PdfMerger()
        #for pdf in pdf_files:
        #    pdf_merger.append('temp.pdf')
        #print(pdf_merger)
    #pdf_merger.write(output_filename)

    # Merge the downloaded PDF files using the PyPDF2 library
    pdf_merger = PdfMerger()
    for file in pdf_files:
        with open(file, 'rb') as f:
            pdf_merger.append(PdfReader(BytesIO(f.read())))
    pdf_merger.write(output_filename)

    for link in drive_links:
        #pdf_files = []
        file_id = link.split('/')[-2]
        if os.path.exists(file_id):
            os.remove(file_id)


