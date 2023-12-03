# TextToVideo
 
Создание видео с пролетающим текстом

## Инструкция по запуску
1. [Скачать и установить Python](https://www.python.org/downloads/)
2. Клонировать данный репозиторий:
```
git clone https://github.com/DogeOk/hackathon.git
```
3. Переместиться в каталог репозитория:
```
cd TextToVideo/text_to_video
```
4. (Рекомендуется) Создать виртуальное окружение:
```
python -m venv venv
```
5. Активировать виртуальное окружение (если было создано):
   + Windows:
   ```
   .\venv\Scripts\activate.ps1
   ```
   + macOS или Linux:
   ```
   source venv/bin/activate
   ```
6. Установить необходимые пакеты из файла `requirements.txt`:
```
pip install -r requirements.txt
```
7. Запустить проект:
```
python manage.py runserver
```
## Docker
1. Собрать образ
```
docker build -t text_to_video:latest https://github.com/DogeOk/TextToVideo.git#main:.
```
2. Запустить контейнер
```
docker run -d -p 8000:8000 text_to_video:latest
```
## Инструкция по использованию
Отправьте GET запрос по адресу `host/text_to_video/?message=Запрос`. Пример приведён ниже
```
http://127.0.0.1:8000/text_to_video/?message=test
```
