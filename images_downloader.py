import requests
import os
from urllib.parse import urlsplit
from pathlib import Path


def extract_extension(url):
    path = urlsplit(url).path
    extension = os.path.splitext(path)[1]
    return extension


def download_image(url, path, filename, params={}):
    Path(path).mkdir(parents=True, exist_ok=True)
    response = requests.get(url, params=params)
    response.raise_for_status()
    extension = extract_extension(url)
    with open(f'{os.path.join(path, filename)}{extension}', 'wb') as file:
        file.write(response.content)
