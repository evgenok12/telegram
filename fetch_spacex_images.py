import requests
import images_downloader
import argparse


def main():
    parser = argparse.ArgumentParser(description='скачивает фотографии запуска spaceX')
    parser.add_argument('-id', '--launch_id', help='номер запуска spaceX', default='latest')
    parser.add_argument('-p', '--path', help='куда сохранить фотографии', default='images')
    args = parser.parse_args()

    try:
        print('Работаем')
        response = requests.get(f'https://api.spacexdata.com/v5/launches/{args.launch_id}')
        response.raise_for_status()
        urls = response.json()['links']['flickr']['original']
        for index, url in enumerate(urls):
            images_downloader.download_image(url, args.path, f'spaceX_{index}')
        if not urls:
            print('Фотографии не найдены')
    except requests.exceptions.HTTPError:
        print('Некорректный номер запуска')
    else:
        print('Скрипт завершил работу')
    

if __name__ == '__main__':
    main()   
    