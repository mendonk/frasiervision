import requests
from bs4 import BeautifulSoup
import os
import re

url = 'https://catsnguitars.wordpress.com/scripts-archive/'
folder_path = './pdfs'  # Replace with your local folder path

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('a'):
    if re.match(r'\[\d+\.\d+\]', link.text):  # Regex to match the pattern [number.number]
        pdf_url = link.get('href')
        if not pdf_url.startswith('http'):
            pdf_url = url + pdf_url  # Constructing the full URL if it's relative
        pdf_response = requests.get(pdf_url)
        pdf_name = pdf_url.split('/')[-1]
        with open(os.path.join(folder_path, pdf_name), 'wb') as f:
            f.write(pdf_response.content)

# this scraper pulls ALL the PDFs. Use the regular script_scraper to just pull 3 PDFs.


