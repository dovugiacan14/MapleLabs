import os 
import requests 
from bs4 import BeautifulSoup 
"/api/download/models/142180"

file_urls = [
    "https://civitai.com/api/download/models/15236",
    # "https://civitai.com/api/download/models/24365",
    # "https://civitai.com/api/download/models/11745",
    # "https://civitai.com/api/download/models/22031",
    # "https://civitai.com/api/download/models/38904",
    # "https://civitai.com/api/download/models/39386"
]

file_names = [
    "Deliberate.safetensors", 
    # "DreamShaper.safetensors", 
    # "ChilloutMix.safetensors", 
    # "Cartoonish.safetensors", 
    # "TFM-American-Cartoons.safetensors", 
    # "CartoonStyleClassic.safetensors"
]

if len(file_urls) > 0: 
    output_path = 'models'
    os.makedirs(output_path, exist_ok= True)
    for file_url, file_name in zip(file_urls, file_names):
        file_path = os.path.join(output_path, file_name)

        response = requests.get(file_url)
        if response.status_code == 200: 
            with open(file_path, "wb") as model:
                model.write(response.content)
            print('Download Successfully')

        else:
            print('Download Failed')