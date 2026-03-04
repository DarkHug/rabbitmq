import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='test_queue')

print('[?] Waiting for message')


def callback(ch, method, properties, body):
    print(f"[x] Received {body.decode()}")


channel.basic_consume(
    queue='test_queue',
    on_message_callback=callback,
    auto_ack=True
)

channel.start_consuming()
