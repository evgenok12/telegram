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
        '-m', '--mode', choices=['image', 'images'], default='image',
        help='image - опубликовать 1 фотографию, images - опубликовать несколько фотографий'        
        )
    parser.add_argument('-p', '--path', help='откуда брать фотографии', default='images')
    args = parser.parse_args()

    telegram_token = env('TELEGRAM_TOKEN')
    telegram_wait_seconds = env.int('TELEGRAM_WAIT_SECONDS', default=14400)
    telegram_chat_id=env('TELEGRAM_CHAT_ID')

    try:
        print('Работаем')        
        bot = telegram.Bot(token=telegram_token)
        if args.mode == 'images' and os.path.isdir(args.path):
            images_paths = [os.path.join(path, name) for path, _, names in os.walk(args.path) for name in names]
            while True:
                for image_path in images_paths:
                    send_photo(image_path, bot, telegram_chat_id)
                    print(f'Фотография опубликована. Cледующая будет опубликована через {telegram_wait_seconds} секунд')
                    time.sleep(telegram_wait_seconds)   
                random.shuffle(images_paths)
        elif args.mode == 'image' and os.path.isfile(args.path):
            send_photo(args.path, bot, telegram_chat_id)
            print('Фотография опубликована')
        else:
            print('Некорректный ввод')
    except telegram.error.TelegramError:
        print('Ошибка')
    

if __name__ == '__main__':
    main()
    