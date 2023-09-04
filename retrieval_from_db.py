#!/usr/bin/env python
# coding: utf-8

# In[43]:


from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma 
import os
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI


# In[44]:


#PUT YOUR API KEY
os.environ["OPENAI_API_KEY"]="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"
#CHANGE db TO YOUR DATABASE NAME
persist_directory='FAQ_bot(8)'
embedding=SentenceTransformerEmbeddings(model_name='all-MiniLM-L6-v2')


# In[45]:


#loading persisted db from disk
vectordb= Chroma(persist_directory= persist_directory, embedding_function=embedding)


# In[46]:


# Making a retriver
retriever= vectordb.as_retriever()


# In[47]:


#Using RetrievalQA Chain for results
qa_chain= RetrievalQA.from_chain_type(llm=OpenAI(),
                                     chain_type='stuff',
                                     retriever=retriever)


# In[48]:


#Defining a function for results
def process_llm_response(llm_response):
    print(llm_response['result'])


# In[49]:


#Creating a Chatbot
flag=True
print("Hi! I am a bot who is here to help. For  ending convo type Bye")
while (flag==True):
    user_response=input()
    user_response=user_response.lower()
    if (user_response!='Bye'):
        if (user_response== 'thank you' or user_response== 'thanks'):
            flag=False
            print("Bot: Welcome")    
        else:
            query= user_response
            llm_response= qa_chain(query)
            process_llm_response(llm_response)
    else:
        flag=False
        print('Bot:Goodbye')


# In[ ]:





# In[ ]:




