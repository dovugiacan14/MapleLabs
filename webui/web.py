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
    "denoising_strength": 0.2, 
    "cfg_scale": 7
}

response = requests.post(url= f'{url}/sdapi/v1/txt2img', json= payload)

r = response.json()

for i in r['images']: 
    image = base64.b64decode(i.split(",",1)[0])

    output_image_path = 'output_image.png'

    with open(output_image_path, "wb") as output_file:
        output_file.write(image)

    print('Image saved to: ', output_image_path)


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'image/png')
        self.end_headers()
        with open("output_image.png", 'rb') as image_file:
            self.wfile.write(image_file.read())

with socketserver.TCPServer(("",PORT), Handler) as httpd:
    print(f'Serving at port {PORT}')
    httpd.serve_forever()
