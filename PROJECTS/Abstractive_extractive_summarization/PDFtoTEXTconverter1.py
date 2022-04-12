import fitz  # this is pymupdf
import re
import os
os.chdir(r"C:\Users\LENOVO\OneDrive\Desktop\PDF files")
for i in range(0,1000):
    with fitz.open("doc"+str(i)+".pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()
        with open("doc"+str(i)+".txt", "w", encoding='utf-8') as f:
            f.write(text)
        
     
