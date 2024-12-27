FROM python:3.12.6

WORKDIR /app

COPY . /app/

RUN apt-get update -y

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD [ "bash", "/app/entrypoint.sh" ]

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# CMD [ "--bind", "0.0.0.0:8000", "kjpanel.wsgi:application"]


