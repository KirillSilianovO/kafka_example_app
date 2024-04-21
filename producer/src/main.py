import os
import random
import time
from datetime import datetime

from kafka import KafkaProducer

kafka_host = os.getenv('KAFKA_HOST', 'localhost')
kafka_port = os.getenv('KAFKA_PORT', '9094')
topik = os.getenv('KAFKA_TOPIC', 'example_topik')
bootstrap_server = f'{kafka_host}:{kafka_port}'

if __name__ == "__main__":

    while True:
        try:
            producer = KafkaProducer(bootstrap_servers=bootstrap_server)
            break
        except Exception as e:
            print(f"Error connecting to Kafka: {e}")
            time.sleep(1)

    i = 1
    while True:
        message = f"Test message number {i}"
        future = producer.send(topik, bytes(message, encoding='utf-8'))
        result = future.get(timeout=2)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        print(f'[{timestamp}] [PRODUCER] <-- Sent message: "{message}"')
        i += 1
        time.sleep(random.randint(1, 3))
