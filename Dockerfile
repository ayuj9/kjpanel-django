FROM python:3.12.4-slim-bullseye

ENV PYTHONBUFFERED=1 



WORKDIR /app
COPY . /app/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "kjpanel.wsgi:application"]


