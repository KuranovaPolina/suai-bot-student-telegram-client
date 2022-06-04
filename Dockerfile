FROM python:3.9-buster
WORKDIR /src
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python3", "bot.py" ]
