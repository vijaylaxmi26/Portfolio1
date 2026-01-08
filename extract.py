import PyPDF2

pdf = PyPDF2.PdfReader('Vijaylaxmi_resume.pdf')
text = ''
for page in pdf.pages:
    text += page.extract_text()
print(text)