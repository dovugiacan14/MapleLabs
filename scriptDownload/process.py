import json 
import requests 
import os 
from bs4 import BeautifulSoup 

# Read configs.json content 
with open('configs.json', 'r') as f: 
    configs = json.load(f)

urls = configs['urls']
title = configs['title_id']
download_id = configs['download_id']

headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"}
output_path = 'models' 
os.makedirs(output_path, exist_ok= True) 

for url in urls: 
    page = requests.get(url= url, headers= headers) 
    soup = BeautifulSoup(page.content, 'html.parser')

    # Get file name 
    model_name = soup.find('h1', class_ = title).text
    file_name = model_name.replace(" ", "")
    file_model_name = file_name + '.safetensors'
    print("Downloading....{}".format(model_name)) 

    # Get link download model 
    download_link_tail = soup.find('a', class_ = download_id).get('href')
    download_link_head = 'https://civitai.com'
    download_link = download_link_head + download_link_tail 

    # Download model processing 
    file_path = os.path.join(output_path, file_model_name)
    response = requests.get(download_link)
    if response.status_code == 200: 
        with open(file_path, "wb") as model:
            model.write(response.content)
        print("Download {} checkpoint successfully".format(model_name))

    else: 
        print("Download {} checkpoint falied.!".format(model_name))
        continue


