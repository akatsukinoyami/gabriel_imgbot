FROM python:3.8-slim-buster
WORKDIR /app/
COPY ./pyrogram.txt ./
RUN ["pip3", "install", "-r", "pyrogram.txt"]
COPY ./requirements.txt ./
RUN ["pip3", "install", "-r", "requirements.txt"]
COPY . .
CMD ["python3", "-m", "bot"]
