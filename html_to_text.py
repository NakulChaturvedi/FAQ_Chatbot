#!/usr/bin/env python
# coding: utf-8

# In[9]:


import requests
from bs4 import BeautifulSoup
urls = ""
response = requests.get(urls)
file= ''
if response.status_code == 200:
    html_content = response.content

    soup = BeautifulSoup(html_content, "html.parser")

    extracted_text = soup.get_text()
    with open(file,'w',encoding='utf-8')as file:
        file.write(extracted_text)
    print("HTML content extracted and saved")
else:
    print(f'Failed.Status_code: {response.status_code}')


# In[10]:


print(extracted_text)


# In[11]:


import html2text
file= ""#FILE PATH FOR STORING CLEAN TEXTS
file_read= open(file, 'r',encoding= 'utf-8')
html_content= file_read.read()
converter = html2text.HTML2Text()
cleaned_text = converter.handle(html_content)

with open(file, 'w',encoding= 'utf-8' )as file:
    file.write(cleaned_text)

print("HTML tags removed and cleaned content.")


# In[ ]:




