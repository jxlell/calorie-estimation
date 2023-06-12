import requests
import os

with open('links.txt', 'r') as file:
    links = file.readlines()

folder_path = 'images'
os.makedirs(folder_path, exist_ok=True)
for link in links:
    response = requests.get(link.strip())
    if response.status_code == 200:
        with open(os.path.join(folder_path, link.split('/')[-1]), 'wb') as img_file:
            img_file.write(response.content)
            print(f'{link.strip()} downloaded successfully.')
    else:
        print(f'Error downloading {link.strip()}.')
