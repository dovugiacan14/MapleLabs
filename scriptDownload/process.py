import json 

# Read configs.json content 
with open('configs.json', 'r') as f: 
    configs = json.load(f)

urls = configs['urls']
print(urls)