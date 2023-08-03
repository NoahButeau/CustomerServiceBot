from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import KafkaError
import time
import sys

# Kafka bootstrap server configuration
bootstrap_servers = 'localhost:9092'

# Topic name
topic = 'test-topic'

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# Produce a message
message = 'testing!'
producer.send(topic, message.encode('utf-8'))

# Wait for the message to be sent
producer.flush()

# Create a Kafka consumer
consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers)


# Consume messages from the topic

for message in consumer:
    print(f'Received message: {message.value.decode("utf-8")}')


# Close the Kafka consumer and producer
consumer.close()
producer.close()