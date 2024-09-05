import pika
import psycopg2
import json

def callback(ch, method, properties, body):
    data = json.loads(body)

    with psycopg2.connect("dbname='demo' user='astra' password='astra' host='db' port='5432'") as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO requests (surname, name, patronym, phone, message) VALUES (%s, %s, %s, %s, %s)",
                (data['surname'], data['name'],
                 data['patronym'], data['phone'], data['message'])

            )
            conn.commit()


def main():
    conn = pika.BlockingConnection(
            pika.ConnectionParameters(host='iprabbitmq', port=5672, credentials=pika.PlainCredentials('astra', 'astra')))
    ch = conn.channel()

    ch.queue_declare(queue='requests')
    ch.basic_consume(queue='requests',
                     on_message_callback=callback, auto_ack=True)
    ch.start_consuming()


if __name__ == "__main__":
    main()
