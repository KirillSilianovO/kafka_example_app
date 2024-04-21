import os
import time
from datetime import datetime

from kafka import KafkaConsumer

kafka_host = os.getenv('KAFKA_HOST', 'localhost')
kafka_port = os.getenv('KAFKA_PORT', '9094')
topik = os.getenv('KAFKA_TOPIC', 'example_topic')
bootstrap_server = f'{kafka_host}:{kafka_port}'

if __name__ == "__main__":

    while True:
        try:
            consumer = KafkaConsumer(topik, bootstrap_servers=bootstrap_server)
            break
        except Exception as e:
            print(f"Error connecting to Kafka: {e}")
            time.sleep(1)

    for message in consumer:
        message_offset = message.offset
        message_data = message.value.decode('utf-8')
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        print(f'[{timestamp}] [CONSUMER] --> Receiving message : "{message_data}" with offset: {message_offset}')
