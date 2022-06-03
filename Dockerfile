FROM python:3.9-buster
<<<<<<< Updated upstream
ENV BOT_NAME=$BOT_NAME

WORKDIR src/app/"${BOT_NAME:-tg_bot}"

COPY requirements.txt /usr/src/app/"${BOT_NAME:-tg_bot}"
RUN pip install -r /usr/src/app/"${BOT_NAME:-tg_bot}"/requirements.txt
COPY . /usr/src/app/"${BOT_NAME:-tg_bot}"
=======
WORKDIR /src
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python3", "bot.py" ]
>>>>>>> Stashed changes
