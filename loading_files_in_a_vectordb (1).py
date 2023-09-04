#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
from langchain.document_loaders import DirectoryLoader
from transformers import GPT2TokenizerFast
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma 
import chromadb


# In[1]:


os.environ["OPENAI_API_KEY"]="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"
#Reads the text file
directory=('')
def load_files(directory):
    loader= DirectoryLoader(directory)
    documents=loader.load()
    return documents
documents= load_files(directory)
len(documents)


# In[5]:


#Tokenization 
tokenizer= GPT2TokenizerFast.from_pretrained('gpt2')
def count_token(text: str)-> int:
    return len(tokenizer.encode(text))
#Chunking
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=40)
texts = text_splitter.split_documents(documents)
len(texts)


# In[6]:


embeddings= SentenceTransformerEmbeddings(model_name='all-MiniLM-L6-v2')


# In[7]:


#Storing data in database using vectordb 
vectordb= Chroma.from_documents(documents=texts,
                               embedding=embeddings,
                               #CHANGE db TO YOUR DATABASE NAME
                               persist_directory='FAQ_bot(8)')


# In[ ]:


#persisting the database to disk 
vectordb.persist()


# In[ ]:


# Storing again
directory=('C:/Users/nakul.chaturvedi/Desktop/cleaned_html')
def load_files(directory):
    loader= DirectoryLoader(directory)
    documents=loader.load()
    return documents
documents= load_files(directory)
len(documents)


# In[ ]:


#Tokenization 
tokenizer= GPT2TokenizerFast.from_pretrained('gpt2')
def count_token(text: str)-> int:
    return len(tokenizer.encode(text))
#Chunking
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=40)
texts = text_splitter.split_documents(documents)
len(texts)


# In[ ]:


vectordb= Chroma.from_documents(documents=texts,
                               embedding=embeddings,
                               #CHANGE db TO YOUR DATABASE NAME
                               persist_directory='FAQ_bot(8)')


# In[ ]:


vectordb.persist()


# In[ ]:


#AND AGAIN 
directory=('C:/Users/nakul.chaturvedi/Desktop/update')
def load_files(directory):
    loader= DirectoryLoader(directory)
    documents=loader.load()
    return documents
documents= load_files(directory)
len(documents)


# In[ ]:


tokenizer= GPT2TokenizerFast.from_pretrained('gpt2')
def count_token(text: str)-> int:
    return len(tokenizer.encode(text))
#Chunking
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=40)
texts = text_splitter.split_documents(documents)
len(texts)


# In[ ]:


vectordb= Chroma.from_documents(documents=texts,
                               embedding=embeddings,
                               #CHANGE db TO YOUR DATABASE NAME
                               persist_directory='FAQ_bot(8)')


# In[ ]:


vectordb.persist()


# In[ ]:


# AND UPDATING
directory=('C:/Users/nakul.chaturvedi/Desktop/update(2)')
def load_files(directory):
    loader= DirectoryLoader(directory)
    documents=loader.load()
    return documents
documents= load_files(directory)
len(documents)


# In[ ]:


tokenizer= GPT2TokenizerFast.from_pretrained('gpt2')
def count_token(text: str)-> int:
    return len(tokenizer.encode(text))
#Chunking
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=40)
texts = text_splitter.split_documents(documents)
len(texts)


# In[ ]:


vectordb= Chroma.from_documents(documents=texts,
                               embedding=embeddings,
                               #CHANGE db TO YOUR DATABASE NAME
                               persist_directory='FAQ_bot(8)')


# In[ ]:


vectordb.persist()


# In[2]:


vectordb.get()


# In[26]:


# directory=('C:/Users/nakul.chaturvedi/Desktop/cleaned')
# def load_files(directory):
#     loader= DirectoryLoader(directory)
#     documents=loader.load()
#     return documents
# documents= load_files(directory)
# len(documents)


# In[31]:


# tokenizer= GPT2TokenizerFast.from_pretrained('gpt2')
# def count_token(text: str)-> int:
#     return len(tokenizer.encode(text))
# #Chunking
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=40)
# texts = text_splitter.split_documents(documents)
# len(texts)


# In[45]:


# ids = [str(i) for i in range(1, len(documents) + 1)]

# # add data
# vectordb= Chroma.from_documents(docs, embedding_function, ids=ids)
# docs = vectordb.similarity_search(query)
# print(docs[0].metadata)

# # update the metadata for a document
# docs[0].metadata = {
#     "source": "C:/Users/nakul.chaturvedi/Desktop/cleaned/cleaned_html(9).txt",
#     "new_value": "hello world",
# }
# vectordb.update_document(ids[0], docs[0])
# print(example_db._collection.get(ids=[ids[0]]))


# In[ ]:




