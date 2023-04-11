# Космический Телеграм
Скачивает фотографий NASA APOD, NASA EPIC, запуска spaceX и публикует их в телеграм канале.

## Окружение
### Зависимости
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```bash
pip install -r requirements.txt
```

### Переменные окружения
#### `fetch_nasa_apod.py` и `fetch_nasa_epic.py`
- NASA_TOKEN=DEMO_KEY
#### `telegram_poster.py`
- TELEGRAM_TOKEN
- TELEGRAM_CHAT_ID
- TELEGRAM_WAIT_SECONDS=14400

1. Поместите файл `.env` рядом со скриптами.
2. `.env` содержит текстовые данные без кавычек.

Например, если вы распечатаете содержимое `.env`, то увидите:

```bash
$ cat .env
NASA_TOKEN=DEMO_KEY
TELEGRAM_TOKEN=123:abc123
TELEGRAM_CHAT_ID=@abc123
TELEGRAM_WAIT_SECONDS=14400
```

#### Как получить `NASA_TOKEN`
Зарегистрируйтесь на [api.nasa.gov](https://api.nasa.gov/#signUp)

#### Как получить `TELEGRAM_TOKEN`
Создайте бота у [@BotFather](https://telegram.me/BotFather)

#### Как получить `TELEGRAM_CHAT_ID`
Это ссылка на телеграм канал, типа @news24

#### Как получить `TELEGRAM_WAIT_SECONDS`
Это время в секундах между публикациями

## Как запустить
Файл `images_downloader.py` должен быть рядом с запускаемыми скриптами
### `fetch_nasa_apod.py`
Запуск на Linux(Python 3) или Windows:

```bash
$ python fetch_nasa_apod.py [-a AMOUNT] [-p PATH]
```
Вы увидите:

```
Работаем
Скрипт завершил работу
```

### `fetch_nasa_epic.py`
Запуск на Linux(Python 3) или Windows:

```bash
$ python fetch_nasa_epic.py [-p PATH] date
```
Вы увидите:

```
Работаем
Скрипт завершил работу
```

### `fetch_spacex_images.py`
Запуск на Linux(Python 3) или Windows:

```bash
$ python fetch_spacex_images.py [-id LAUNCH_ID] [-p PATH]
```
Вы увидите:

```
Работаем
Скрипт завершил работу
```

### `telegram_poster.py`
Запуск на Linux(Python 3) или Windows:

```bash
$ python telegram_poster.py {image,images} path 
```
Вы увидите:

```
Работаем
Фотография опубликована. Cледующая будет опубликована через 14400 секунд
```
или
```
Фотография опубликована
```

Используйте `--help`, чтобы посмотреть информацию о скриптах.
```bash
$ python my_script --help

