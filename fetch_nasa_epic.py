import requests
import images_downloader
import argparse
from datetime import datetime
from environs import Env


def main():
    env = Env()
    env.read_env()

    parser = argparse.ArgumentParser(description='скачивает фотографии NASA EPIC')
    parser.add_argument('date', help='дата (день.месяц.год)')
    parser.add_argument('-p', '--path', help='куда сохранить фотографии', default='images')
    args = parser.parse_args()

    nasa_token = env('NASA_TOKEN', default='DEMO_KEY')
    params = {
        'api_key': nasa_token,
    } 

    date = datetime.strptime(args.date, '%d.%m.%Y')
    day, month, year = date.day, date.month, date.year

    try:
        print('Работаем')
        response = requests.get(f'https://epic.gsfc.nasa.gov/api/natural/date/{year}-{month:02}-{day:02}', params=params)
        response.raise_for_status()
        images = response.json()
        if not images:
            print('Фотографии не найдены')
        for index, image in enumerate(images):
            image_name = image['image']
            url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month:02}/{day:02}/png/{image_name}.png'
            images_downloader.download_image(url, args.path, f'nasa_epic_{index}', params)
    except requests.exceptions.HTTPError:
        print('Ошибка соединения')
    else:
        print('Скрипт завершил работу')
    

if __name__ == '__main__':
    main()
    