import json, os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin.settings')
django.setup()
import pika

from products.models import Product

params = pika.URLParameters('amqps://sdelsnmz:iFTN6WyUju8lZNKQzUEEbqy9_ML_0ZTt@stingray.rmq.cloudamqp.com/sdelsnmz')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    data = json.loads(body)
    print(id)
    product = Product.objects.get(id=data)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased')

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('started consuming')
channel.start_consuming()
channel.close()
