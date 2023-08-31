from django.shortcuts import render
from django.http import HttpResponse 
import base64 
import requests

from PIL import Image 
from io import BytesIO


url = "http://127.0.0.1:7860"

payload = {
    "prompt": "A picture of a boy, garden background",
    "steps": 30, 
    "denoising_strength": 0.4, 
    "cfg_scale": 7, 
    "styles": ["anime"], 
    "batch_size": 1
}

response = requests.post(url= f'{url}/sdapi/v1/txt2img', json= payload)

r = response.json()

# Create your views here.
def show_image(request):

    for i in r['images']: 
        img = base64.b64decode(i.split(",",1)[0])

        image = Image.open(BytesIO(img))

        img_io = BytesIO()

        image.save(img_io, 'PNG')

        img_io.seek(0)

    response = HttpResponse(img_io, content_type = 'image/png')

    return response 
