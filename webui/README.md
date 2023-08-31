# Image Project web 
A source code demo of image generation from the input prompt based on using text-to-image API from Stable Diffusion webUI (http://127.0.0.1:7860//sdapi/v1/txt2img)
Souce course is built based on Django framework 

# Installation and Running 
1. Install [Python 3.10.6], checking "Add Python to PATH" 
2. Download the stable-diffusion-webui repository, for example by running "git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git"  
3. Install required libraries 
3. Run ./webui.sh -- api in command line 
4. Then, keep the command line running anf open another comamand line 
5. Install Django (pip install Django)
6. cd ImageProject 
7. Running web by "python manage.py runserver" command 

# Using 
1. Enter prompt as Json. Example: {'prompt: A picture of a house, 'negative prompt': 'people, garden'}
2. Enter generate 
3. Use can custom the number of images you want to generate by changing 'batch_size' in Json syntax input 
Ex: If you want generate 5 images, you can run: 
    {'prompt: A picture of a house, 'negative prompt': 'people, garden', 'batch_size': 5}
    