import telegram
from environs import Env
import os
import time
import random
import argparse


def send_photo(photo_path, telegram_bot, telegram_chat_id):
    with open(photo_path, 'rb') as photo:
        telegram_bot.sendPhoto(chat_id=telegram_chat_id, photo=photo)


def main():
    env = Env()
    env.read_env()

    parser = argparse.ArgumentParser(description='публикует фотографии в телеграм канал')
    parser.add_argument(
        '-s', '--shuffle', action='store_true',
        help='если фотографии закончатся, они будут перемешаны, и публикация начнется сначала'        
        )
    parser.add_argument('-p', '--path', help='откуда брать фотографии', default='images')
    args = parser.parse_args()
    if not os.path.isdir(args.path):
        exit('Неверно указана директория')

    telegram_token = env('TELEGRAM_TOKEN')
    telegram_wait_seconds = env.int('TELEGRAM_WAIT_SECONDS', default=14400)
    telegram_chat_id=env('TELEGRAM_CHAT_ID')

    print('Работаем')        
    bot = telegram.Bot(token=telegram_token)
    images_paths = [os.path.join(path, name) for path, _, names in os.walk(args.path) for name in names]

    while True:
        for index, image_path in enumerate(images_paths):
            while True:
                try:
                    send_photo(image_path, bot, telegram_chat_id)
                    print('Фотография опубликована')
                    if args.shuffle or index != len(images_paths) - 1: 
                        print(f'Cледующая будет опубликована через {telegram_wait_seconds} секунд')
                        time.sleep(telegram_wait_seconds)
                    break
                except telegram.error.NetworkError:
                    print('Проблемы с подключением. Переподключение')
                    time.sleep(10)
        if not args.shuffle:
            break
        random.shuffle(images_paths)
        print('Фотографии перемешаны')     
                                       
    print('Скрипт завершил работу')


if __name__ == '__main__':
    main()
    