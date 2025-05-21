""" An example of a kafka producer """

from os import environ

from dotenv import load_dotenv
from confluent_kafka import Producer

if __name__ == "__main__":
    load_dotenv()

    kafka_producer = Producer({
        "bootstrap.servers": environ["BOOTSTRAP_SERVERS"],
        'security.protocol': environ["SECURITY_PROTOCOL"],
        'sasl.mechanisms': environ["SASL_MECHANISM"],
        'sasl.username': environ["USERNAME"],
        'sasl.password': environ["PASSWORD"]
    })

    kafka_producer.produce(topic=environ["TOPIC"],
                           value="HI!")
    
    kafka_producer.produce(topic=environ["TOPIC"],
                           value="Hi again!")
    
    kafka_producer.produce(topic=environ["TOPIC"],
                           value="Its me")
    
    kafka_producer.flush() # wait for all messages to send
