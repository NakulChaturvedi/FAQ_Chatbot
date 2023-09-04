Used Packages:
import os
from langchain.document_loaders import DirectoryLoader
from transformers import GPT2TokenizerFast
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma 
import chromadb
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

1.In the 'loading_files_in_a_vectordb''script, we have used DirectoryLoader to load a folder of text files.
2.Then, we tokenized and chunked the text files in the folder using GPT2TokenizerFast and  RecursiveCharacterTextSplitter
3.Used OpenAI Embedddings to embed the data and then store it in a persistant directory('db) made by chroma.
4. Then we persisted the directory to disk using- vectordb.persist()


1.In the 'retrieval_from_db' script, we defined the variables for OpenAI Embeddings, persistant directory and added the OpenAI key.
2. Then we loaded the persistant database from disk to use it and made a retriever using vectordb.as_retriever()
3. Then we used RetrievalQA Chain for result template and prompts 
4. We then defined a function ehich will give result and feed the right context 
5. Then we created a chatbot which took input from the user and gave an output according to the context in database. 