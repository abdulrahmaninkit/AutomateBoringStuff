#Program 1: This program can read an PDF file.

import PyPDF2 
import os

os.chdir("D:\Computer Languages\Programming Languages\AutomateTheBooringStuffCodes")

#PdfFileReader has been changed to PdfReader from 3.0.0
reader = PyPDF2.PdfReader("sample2.pdf")

#reader.numPages has been changed to len(reader.pages)
print(len(reader.pages))   #To get the total number of pages

page = reader.pages[0].extract_text()   #To read the page 0 from the pdf
print(page)

# To read all the pages in a loop
for PageNum in range(len(reader.pages)):
    page = reader.pages[PageNum].extract_text()   
    print(page)

#----------------------------------------------------------------------------------------------------

#Program 2: To write into an PDF file
import PyPDF2,os

pdf1file = open("Sample1.pdf","rb")
pdf2file = open("sample2.pdf","rb")

reader1 = PyPDF2.PdfReader("Sample1.pdf")
reader2 = PyPDF2.PdfReader("sample2.pdf")

writer = PyPDF2.PdfWriter()

for PageNum in range(len(reader1.pages)):
    page = reader1.pages[PageNum]
    writer.add_page(page)  

for PageNum in range(len(reader2.pages)):
    page = reader2.pages[PageNum]
    writer.add_page(page)  

outputFile = open("combined.pdf","wb")
writer.write(outputFile)
outputFile.close()
pdf1file.close()
pdf2file.close()
