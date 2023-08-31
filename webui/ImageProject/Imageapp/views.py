from django.shortcuts import render
from django.http import HttpResponse 
from django.conf import settings 
from rest_framework.views import APIView
from .forms import * 
import base64 
import requests
import json 
import io 
import os 

from PIL import Image, PngImagePlugin 
from io import BytesIO

# Create your views here.

class ImagePage(APIView):
    def get(self, request, *args, **kwargs):
        form = SearchForm()
        return render(request, template_name= 'Imageapp/index.html', context= {
            'form': form,
        })
    
    def post(self, request, *args, **kwargs): 
        url =  "http://127.0.0.1:7860"
        
        form = SearchForm(request.POST, request.FILES)
        if form.is_valid():
            payload_ = form.cleaned_data['prompt'] 
            payload = json.loads(payload_)

            print(payload)
            print(type(payload))

            response = requests.post(url= f'{url}/sdapi/v1/txt2img', json= payload)
            r = response.json()
        
            processed_image_filenames = []

            for idx, i in enumerate(r['images']):
                image_data = base64.b64decode(i.split(",",1)[0])
                image_filename = f'output_image_{idx}.png'
                
                image_path = os.path.join('staticfiles', 'processed_images', image_filename)
                with open(image_path, "wb") as output_file:
                    output_file.write(image_data)

                processed_image_filenames.append(image_path)
            print(processed_image_filenames)

            # solve 
            return render(request, template_name= 'Imageapp/index.html', context= {
                'processed_image_filenames': processed_image_filenames,
            })
        else: 
            return HttpResponse('Uploaded Fail')