import pika
from sys import exit
import os

total_sum = 0

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='NumbersSum')


def sum_callback(ch, method, properties, body):
    try:
        global total_sum
        recieved_value = int(body)
        print(f'recieved_value: {recieved_value}')
        total_sum += recieved_value
        print(f'TotalSum: {total_sum}')

    except Exception as exc:
        return


def main():
    channel.basic_consume(queue='NumbersSum', on_message_callback=sum_callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    channel.queue_delete('NumbersSum')
    connection.close()
    print(f'total sum: {total_sum}')


if __name__ == '__main__':
    main()







