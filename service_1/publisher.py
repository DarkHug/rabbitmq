import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='test_queue')
channel.basic_publish(exchange='',
                      routing_key='test_queue',
                      body='Almas Soska!')
print("[!] Sent secret message ")
connection.close()
