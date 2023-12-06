import os
import pyperclip

def get_pdf_files(directory):
    pdf_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".pdf"):
                pdf_files.append(os.path.join(root, file))
    return pdf_files

pdf_files_list = get_pdf_files("C:/Users/User/Dropbox/Family Room/TUC Records/Warehouse POD")

pdf_files_str = "\n".join(pdf_files_list)

pyperclip.copy(pdf_files_str)
