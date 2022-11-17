import PyPDF2
import os
#create file object variable
#opening method will be rb
def convert_pdf_to_text(filename):
    pdffileobj=open(filename,'rb')
    
    #create reader variable that will read the pdffileobj
    pdfreader=PyPDF2.PdfFileReader(pdffileobj)
    
    #This will store the number of pages of this pdf file
    x=pdfreader.numPages
    print(x)
    
    for i in range(x):
        pageobj=pdfreader.getPage(i)
        
        text=pageobj.extractText()

        with open("{}{}.txt".format(os.path.splitext(filename)[0],i), "a", encoding="utf-8") as f:
            f.write(text)
    pdffileobj.close()


if __name__ == '__main__':
    convert_pdf_to_text("2.pdf")

