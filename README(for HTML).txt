Packages used:
1.BeautifulSoup(from bs4 import BeautifulSoup)
2.requests
3.urllib.request(from urllib.request import urlopen)
4. re
5.html2text

STEPS:
(EXTRACTING URLs)
1.FIrstly parsed the parent url using BeautifulSoup
2.Used 'html.parser'
3.Then used urllib to create a response from the parent URL
4.Created a list for the child urls produced
5.Used re to filter the URLs to only useful one (which contain '/xref/')
6.Then appended the prefix to those URLs
(STORING URLs)
1.Used requests to get URL for response
2.Used BeautifulSoup to extract the text from URLs
3.Stored it in the desirable file path
(REMOVING HTML TAGS)
1.Used html2text to clean the tags from extracted text
2.Stored it in the desirable file path
(USING DATA IN CHATBOT)
1.Load the files in a vectore db made in 'loading_files_in_a_vectordb.py' script
2.Use them in teh QA Chain made in 'retrieval_from_db' script.