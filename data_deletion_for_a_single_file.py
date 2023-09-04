#!/usr/bin/env python
# coding: utf-8

# In[1]:


import fitz

input_file = r"C:/Users/nakul.chaturvedi/Desktop/TPV181_QFU1.1E&QFU2.1E&QFU1.2E_TV reboot when switching channels.v3docx.pdf"
  
output_file = r"C:/Users/nakul.chaturvedi/Desktop/25.pdf"
  
file_handle = fitz.open(input_file)
  
page = 0
  
file_handle.delete_page(page)
  
file_handle.save(output_file)


# In[2]:


file= 'C:/Users/nakul.chaturvedi/Desktop/25.pdf'
lines=[]


# In[3]:


import pdfplumber
import PyPDF2
with pdfplumber.open(file) as pdf:
     pages= pdf.pages
     for page in pdf.pages:
         text= page.extract_text()
         for line in text.split('\n'):
             lines.append(line)
             print(line)


# In[4]:


pdf_file = "C:/Users/nakul.chaturvedi/Desktop/25.pdf"
text_file = "C:/Users/nakul.chaturvedi/Desktop/25.txt"
pdf = PyPDF2.PdfReader(pdf_file)
text = ""
for page in pdf.pages:
    text += page.extract_text()
with open(text_file, "w",encoding="utf-8") as f:
    f.write(text)


# In[1]:


def remove_text_between(text_file, start_text, end_text):
    with open(text_file, 'r',encoding='utf-8') as file:
        content = file.read()

    start_pos = content.find(start_text)
    end_pos = content.find(end_text)

    if start_pos != -1 and end_pos != -1:
        modified_content = content[:start_pos] + content[end_pos + len(end_text):]
        with open(text_file, 'w',encoding='utf-8') as file:
            file.write(modified_content)


# In[6]:


remove_text_between('C:/Users/nakul.chaturvedi/Desktop/25.txt', "---","Question")


# In[7]:


def print_txt_file(file_path):
        with open(file_path, 'r',encoding='utf-8') as file:
            content = file.read()
            print(content)


# In[8]:


file_path = 'C:/Users/nakul.chaturvedi/Desktop/25.txt'  
print_txt_file(file_path)


# In[ ]:




