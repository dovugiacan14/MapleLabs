import os 
import json 
import requests 
import traceback
from tqdm import tqdm 
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor 

def download_model(url, headers, title, download_id, output_path): 
    try:
        page = requests.get(url= url, headers= headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        # get file name 
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
        response = requests.get(download_link, stream= True)

        
        if response.status_code == 200: 
            total_size = int(response.headers.get('content-length', 0))
            with open(file_path, "wb") as model, tqdm(
                desc= model_name, 
                total= total_size, 
                unit= "B", 
                unit_scale= True, 
                unit_divisor= 1024 
            ) as bar: 
                for data in response.iter_content(chunk_size= 1024):
                    bar.update(len(data))
                    model.write(data)
            print("Download {} checkpoint succesfully.!".format(model_name))
        
    except requests.exceptions.RequestException as e: 
        print("Download {} checkpoint failed! {}".format(model_name, e))
        traceback.print_exc()   # print current error 
        

def main():
    with open('configs.json', 'r') as f: 
        configs = json.load(f)
    
    urls = configs["urls"]
    title = configs["title_id"]
    download_id = configs["download_id"]

    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"}
    output_path = 'models' 
    os.makedirs(output_path, exist_ok= True)

    with ThreadPoolExecutor(max_workers= 4) as executor:
        for url in urls: 
            executor.submit(download_model, url, headers, title, download_id, output_path)

if __name__ == '__main__': 
    main()



    