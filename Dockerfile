FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN python -m snips_nlu download en

COPY . .

CMD [ "flask", "run", "--host=0.0.0.0"]