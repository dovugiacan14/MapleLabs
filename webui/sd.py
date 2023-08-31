import json 
import requests
import io 
import base64 
import http.server 
import socketserver


from PIL import Image, PngImagePlugin 

url = "http://127.0.0.1:7860"
PORT = 8000 

payload = {
    "prompt": "Asene Wenger Coach, Arsenal logo background",
    "steps": 30, 
    "denoising_strength": 0.4, 
    "cfg_scale": 7
}

response = requests.post(url= f'{url}/sdapi/v1/txt2img', json= payload)

r = response.json()

for i in r['images']: 
    image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

    png_payload = {
        "image": "data:image/png;base64, "+ i
    }

    response2 = requests.post(url= f'{url}/sdapi/v1/png-info', json= png_payload)

    png_info = PngImagePlugin.PngInfo()

    png_info.add_text("parameters", response2.json().get("info"))

    image.save("output.png", pnginfo= png_info)