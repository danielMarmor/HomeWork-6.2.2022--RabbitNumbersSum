import pika


def produce_numbers():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='NumbersSum')

    # for i in range(10):
    #     number_str = str(i)
    #     channel.basic_publish(exchange='', routing_key='NumbersSum', body=number_str)

    while True:
        number_str = input('Enter Number: ')
        if number_str == '':
            break
        channel.basic_publish(exchange='', routing_key='NumbersSum', body=number_str)
    connection.close()


if __name__ == '__main__':
    produce_numbers()

