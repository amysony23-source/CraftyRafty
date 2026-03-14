FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install flask flask-sqlalchemy

RUN python database.py

EXPOSE 5000

CMD ["python", "app.py"]


