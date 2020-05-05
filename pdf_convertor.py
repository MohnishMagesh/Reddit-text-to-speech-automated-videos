# C:\Program Files\wkhtmltopdf\bin
import pdfkit
import imgkit

# config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin")
# pdfkit.from_file("C:\\Users\\MOHNISH\\AI\\Reddit_bot\\template\\reddit_post_template.html","sample.pdf")
# from xhtml2pdf import pisa             # import python module
# import urllib2
# # Define your data
# htmlFile = urllib2.urlopen('C:\\Users\\MOHNISH\\AI\\Reddit_bot\\template\\reddit_post_template.html')
# sourceHtml = htmlFile.read()
# outputFilename = "test.pdf"
# destination = "C:\\Users\\MOHNISH\\AI\\Reddit_bot\\template\\"
#
# # Utility function
# def convertHtmlToPdf(sourceHtml, outputFilename):
#     # open output file for writing (truncated binary)
#     resultFile = open(destination + outputFilename, "w+b")
#
#     # convert HTML to PDF
#     pisaStatus = pisa.CreatePDF(
#             sourceHtml,                # the HTML to convert
#             dest=resultFile)           # file handle to receive result
#
#     # close output file
#     resultFile.close()                 # close output file
#
#     # return True on success and False on errors
#     return pisaStatus.err
#
# # Main program
# if __name__ == "__main__":
#     pisa.showLogging()
#     convertHtmlToPdf(sourceHtml, outputFilename)

# filename = "test.pdf"
# destination = "C:\\Users\\MOHNISH\\AI\\Reddit_bot\\template\\"
# template = open("C:\\Users\\MOHNISH\\AI\\Reddit_bot\\template\\reddit_post_template.html")
# pdf = pisa.CreatePDF(template.read(), file(destination + filename, "w"))
# template.close()

# pdfkit.from_file('C:\\Users\\MOHNISH\\AI\\Reddit_bot\\template\\reddit_post_template.html','C:\\Users\\MOHNISH\\AI\\Reddit_bot\\template\\out.pdf')
imgkit.from_file('C:\\Users\\MOHNISH\\AI\\Reddit_bot\\template\\reddit_post_template.html', 'C:\\Users\\MOHNISH\\AI\\Reddit_bot\\template\\out.png')
