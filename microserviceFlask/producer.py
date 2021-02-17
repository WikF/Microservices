import json

import pika

params = pika.URLParameters('amqps://sdelsnmz:iFTN6WyUju8lZNKQzUEEbqy9_ML_0ZTt@stingray.rmq.cloudamqp.com/sdelsnmz')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)

