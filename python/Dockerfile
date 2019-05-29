FROM alpine:latest

USER root

RUN apk update && apk fetch openjdk8 && apk add openjdk8
RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base && pip install click pyinstaller
WORKDIR /app

ADD jenkins-cli.jar cli.py ./

#RUN pyinstaller cli.py

CMD [ "python", "cli.py"]
