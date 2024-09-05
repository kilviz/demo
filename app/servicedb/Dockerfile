FROM python:3.9
WORKDIR /app
RUN pip install  pika psycopg2
COPY . .
CMD ["python", "service.py"]
