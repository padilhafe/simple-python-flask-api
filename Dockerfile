FROM python:3.12.3-alpine3.20

EXPOSE 5000

WORKDIR /app

COPY requirements.txt wsgi.py config/ application/ ./

RUN pip install -r requirements.txt

CMD ["python", "wsgi.py"]