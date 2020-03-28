import PyPDF2

with open('./files/dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('./files/mypdf.pdf', 'wb') as newFile:
        writer.write(newFile)




