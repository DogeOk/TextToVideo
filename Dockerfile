FROM python:3.10-slim
RUN apt-get update
RUN apt-get install -y python3-opencv
COPY text_to_video /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
