#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import PyPDF2

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

def main():
    input_folder = "C:/Users/nakul.chaturvedi/Desktop/pdfs(4)"
    page_to_remove = 1

    if not os.path.exists(input_folder):
        print("Input folder does not exist.")
        return

    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_folder, filename)
            remove_page_from_pdf(pdf_path, page_to_remove)

    print("Page removal completed!")

if __name__ == "__main__":
    main()


# In[4]:


import os
import PyPDF2

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
    input_folder = "C:/Users/nakul.chaturvedi/Desktop/pdfs(4)"
    output_folder = "C:/Users/nakul.chaturvedi/Desktop/pdfs(text)(4)"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_folder, filename)
            text = pdf_to_text(pdf_path, output_folder)
            save_text_to_file(text, output_folder, os.path.splitext(filename)[0])
    
    print("Conversion completed!")


# In[5]:


if __name__ == "__main__":
    main()


# In[6]:


def remove_text_between(file_path, start_text, end_text):
    with open(file_path, 'r',encoding='utf-8') as file:
        content = file.read()

    start_pos = content.find(start_text)
    end_pos = content.find(end_text)

    if start_pos != -1 and end_pos != -1:
        modified_content = content[:start_pos] + content[end_pos + len(end_text):]
        with open(file_path, 'w',encoding= 'utf-8') as file:
            file.write(modified_content)

def process_files_in_folder(folder_path, start_text, end_text):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        remove_text_between(file_path, start_text, end_text)


# In[7]:


folder_path= "C:/Users/nakul.chaturvedi/Desktop/"
start_text= "---"
end_text= "Question"


# In[8]:


process_files_in_folder(folder_path, start_text, end_text)


# In[ ]:




