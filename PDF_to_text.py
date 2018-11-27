import PyPDF2
from nltk.tokenize import word_tokenize
import re

filename = 'C:\\Python\\Cocoa.pdf' 
pdfFileObj = open(filename,'rb')
 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
num_of_pages = pdfReader.numPages
count = 0
text = ""
 
while count < num_of_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()

text=re.sub("[^a-zA-Z\n]"," ",text)


file=open("final.txt","w")


file.write(text)


file.close()
