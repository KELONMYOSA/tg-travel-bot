### .env example

```
BOT_TOKEN=TgB0tT0k3N
DATABASE_HOST=127.0.0.1
DATABASE_PORT=5432
DATABASE_NAME=database
DATABASE_USER=username
DATABASE_PASSWORD=pass123
```

### Dockerfile

```
FROM python
RUN git clone https://github.com/KELONMYOSA/tg-travel-bot
WORKDIR tg-travel-bot
COPY .env .env
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
```

### Docker build

```
docker build --no-cache -t python-travel-bot-image .
```

### Docker run

```
docker run -d --name python-travel-bot --restart always python-travel-bot-image
```