import requests
from bs4 import BeautifulSoup
import os
import re

url = 'https://catsnguitars.wordpress.com/scripts-archive/'
folder_path = './pdfs'  # Replace with your local folder path
if not os.path.exists(folder_path):
    os.mkdir(folder_path)
    print("Directory '%s' created" % folder_path)
else:
    print("Directory '%s' already exists" % folder_path)

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

pdf_counter = 0  # Initialize a counter for the number of PDFs downloaded

for link in soup.find_all('a'):
    if re.match(r'\[\d+\.\d+\]', link.text):  # Regex to match the pattern [number.number]
        if pdf_counter < 3:  # Check if less than 3 PDFs have been downloaded
            pdf_url = link.get('href')
            if not pdf_url.startswith('http'):
                pdf_url = url + pdf_url  # Constructing the full URL if it's relative
            pdf_response = requests.get(pdf_url)
            pdf_name = pdf_url.split('/')[-1]
            with open(os.path.join(folder_path, pdf_name), 'wb') as f:
                f.write(pdf_response.content)
            pdf_counter += 1  # Increment the counter after a PDF is downloaded
        else:
            break  # Break the loop if 3 PDFs have been downloaded
