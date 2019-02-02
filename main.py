# File: Hello.py
# print(char['text'].encode('utf-8'))
import pdfplumber

with pdfplumber.open("./resume.pdf") as pdf:
    dictionary={}
    count=0
    for page in pdf.pages: 
        for char in page.chars :
            dictionary[count] = [char['text'],char['x0'],char['y0'],char['fontname'],char['size']]
            count+=1
    for x in range(0,count):
        print(dictionary[x])
    print(count)
