""" an example of a kafka consumer """

from os import environ

from dotenv import load_dotenv
from confluent_kafka import Consumer

def consume_messages(cons: Consumer) -> None:
    while True:
        msg = cons.poll(1.0)
        if msg:
            print(msg.value().decode(), msg.offset(), msg.error())

if __name__ == "__main__":
    load_dotenv()

    consumer = Consumer({
        "bootstrap.servers": environ["BOOTSTRAP_SERVERS"],
        "group.id": environ["GROUP"],
        "auto.offset.reset": environ["AUTO_OFFSET"],
        'security.protocol': environ["SECURITY_PROTOCOL"],
        'sasl.mechanisms': environ["SASL_MECHANISM"],
        'sasl.username': environ["USERNAME"],
        'sasl.password': environ["PASSWORD"]
    })

    consumer.subscribe([environ["TOPIC"]])
    consume_messages(consumer)
