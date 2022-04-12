import os

import requests

from urllib.parse import urljoin

from bs4 import BeautifulSoup

url = "https://aclanthology.org/volumes/D18-1/" #Website from where PDFs are to be extracted

folder_location = r'E:\NewPDFfile'

if not os.path.exists(folder_location):os.mkdir(folder_location)

response = requests.get(url)

soup= BeautifulSoup(response.text, "html.parser")     

for link in soup.select("a[href$='.pdf']"):

    #Name the pdf files using the last portion of each link which are unique in this case

    filename = os.path.join(folder_location,link['href'].split('/')[-1])

    with open(filename, 'wb') as f:

        f.write(requests.get(urljoin(url,link['href'])).content)
