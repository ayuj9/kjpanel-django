FROM python:3.12.4-slim-bullseye

WORKDIR /app

COPY . /app/

COPY requirements.txt ./

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=kjpanel.settings

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "kjpanel.wsgi:application"]


