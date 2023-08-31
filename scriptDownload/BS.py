from bs4 import BeautifulSoup 
import urllib.request 
import requests
import os 


url = "https://civitai.com/models/4823/deliberate"



headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"}

page = requests.get(url= url, headers= headers)
soup = BeautifulSoup(page.content, 'html.parser')


# Get file name 
model_name = soup.find('h1' ,class_ = 'mantine-Text-root mantine-Title-root mantine-1tq2xbx').text
file_name = model_name.replace(" ", "")
file_model_name = file_name + '.safetensors'
print(file_model_name)


# Get link download model 
download_link_tail = soup.find('a', class_ = 'mantine-UnstyledButton-root mantine-Button-root mantine-zj7kjy').get('href')
download_link_head = "https://civitai.com"
download_link = download_link_head + download_link_tail 
print(download_link)

# download model processing 
output_path = 'models' 
os.makedirs(output_path, exist_ok= True)
file_path = os.path.join(output_path, file_model_name)
respone = requests.get(download_link)
if respone.status_code == 200: 
    with open(file_path, 'wb') as model: 
        model.write(respone.content)
    
    print("Download Successfully")

else:
    print("Download Failed")

