from PyPDF2 import PdfFileMerger, PdfFileReader

filenames = ["bps_1.pdf", "bps_2.pdf"]

merger = PdfFileMerger()
for filename in filenames:
    merger.append(PdfFileReader(open(filename, 'rb')))

merger.write("bps.pdf")