# import PyPDF2
#
# FILE_PATH = '5_6064436209260691787.pdf'
#
# with open(FILE_PATH, mode='rb') as f:
#
#     reader = PyPDF2.PdfFileReader(f)
#
#     page = reader.getPage(0)
#
#     print(page.extractText())
#

# import os
# import subprocess
#
# for top, dirs, files in os.walk('/home/sitharth/quarantine/python_examples/check'):
#     for filename in files:
#         if filename.endswith('.pdf'):
#             abspath = os.path.join(top, filename)
#             subprocess.call('lowriter --invisible --convert-to doc "{}"'
#                             .format(abspath), shell=True)


import PyPDF2
pdffileobj=open('sitharthan_C_Developer Resume.pdf','rb')
pdfreader=PyPDF2.PdfFileReader(pdffileobj)
x=pdfreader.numPages
pageobj=pdfreader.getPage(x-1)
text=pageobj.extractText()

file1=open(r"sitharthan_C_Developer Resume.txt","a")
file1.writelines(text)
file1.close()
