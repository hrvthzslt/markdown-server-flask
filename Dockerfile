FROM python:3.12-slim

COPY . /app

RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt

WORKDIR /app

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
