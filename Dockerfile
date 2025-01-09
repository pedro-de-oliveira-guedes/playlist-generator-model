FROM python:3.11-slim-bullseye

WORKDIR /app

COPY main.py /app
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "main.py"]
