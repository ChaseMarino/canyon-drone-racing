import pika, sys, os
import zlib
from data import *
import VehicleStatus_pb2


def consume():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.1.20'))
    channel = connection.channel()
    channel.basic_consume(queue='ui', on_message_callback=callback, auto_ack=True)
    print("Consuming")
    channel.start_consuming()

def callback(ch, method, properties, body):
    if(properties.type == 'status'):
        inflated_body = zlib.decompress(body)
        vehicle_status = VehicleStatus_pb2.VehicleStatus()
        vehicle_status.ParseFromString(inflated_body)
        setTestData(vehicle_status)
        # print(getVehicleData())


