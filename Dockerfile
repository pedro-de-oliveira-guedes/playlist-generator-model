FROM python:3.11-slim-bullseye

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "main.py"]
