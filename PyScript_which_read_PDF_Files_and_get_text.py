#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import PyPDF2
#Removal of table from pdf
def remove_page_from_pdf(pdf_path, page_num):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        if page_num<1 or page_num>len(pdf_reader.pages):
            print(f"Page number {page_num} is invalid for file {pdf_path}. Skipping.")
            return
        pdf_writer= PyPDF2.PdfWriter(pdf_file)

        for page_index in range(len(pdf_reader.pages)):
            if page_index + 1 != page_num:
                page = pdf_reader.pages[page_index]
                pdf_writer.add_page(page)

        
        with open(pdf_path, 'wb') as output_file:
            pdf_writer.write(output_file)

#Converting pdf to text file 
def pdf_to_text(pdf_path, output_dir):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page_number in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]
            text += page.extract_text()
        
    return text

def save_text_to_file(text, output_dir, filename):
    output_path = os.path.join(output_dir, filename + '.txt')
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(text)

def main():
    input_folder = "C:/Users/nakul.chaturvedi/Desktop/New folder (3)"
    page_to_remove = 1

    if not os.path.exists(input_folder):
        print("Input folder does not exist.")
        return

    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_folder, filename)
            remove_page_from_pdf(pdf_path, page_to_remove)
            
input_folder = "C:/Users/nakul.chaturvedi/Desktop/New folder (3)"
output_folder = "C:/Users/nakul.chaturvedi/Desktop/texts(3)"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(input_folder, filename)
        text = pdf_to_text(pdf_path, output_folder)
        save_text_to_file(text, output_folder, os.path.splitext(filename)[0])
    
print("Conversion completed!")

if __name__ == "__main__":
    main()


# In[ ]:




