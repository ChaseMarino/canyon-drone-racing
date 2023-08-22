'''import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
connection.close()'''