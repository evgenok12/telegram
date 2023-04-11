import requests
import images_downloader
import argparse
from environs import Env


def main():
    env = Env()
    env.read_env()

    parser = argparse.ArgumentParser(description='скачивает рандомные фотографий NASA APOD')
    parser.add_argument('-a', '--amount', help='количество фотографий', default=1)
    parser.add_argument('-p', '--path', help='куда сохранить фотографии', default='images')
    args = parser.parse_args()

    nasa_token = env('NASA_TOKEN', default='DEMO_KEY')
    params = {
        'api_key': nasa_token,
        'thumbs': 'True',
        'count': args.amount
    }

    try:
        print('Работаем')
        response = requests.get('https://api.nasa.gov/planetary/apod', params=params)
        response.raise_for_status()
        images = response.json()
        for index, image in enumerate(images):
            if image['media_type'] == 'image':
                images_downloader.download_image(image['url'], args.path, f'nasa_apod_{index}')
            elif image['media_type'] == 'video':
                images_downloader.download_image(image['thumbnail_url'], args.path, f'nasa_apod_{index}')
    except requests.exceptions.HTTPError:
        print('Некорректное количество')
    else:
        print('Скрипт завершил работу')
    

if __name__ == '__main__':
    main()
    