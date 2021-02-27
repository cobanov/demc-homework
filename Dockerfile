FROM python:3.9-alpine

LABEL maintaienr="mertcobanov@gmail.com"

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]

CMD [ "wsgi.py" ]
