
from kafka import KafkaProducer
from kafka import KafkaConsumer
from customerBot import CustomerBot


SERVER ='localhost:9092'
producer = KafkaProducer(bootstrap_servers=SERVER)
#consumer = KafkaConsumer('thisATest',bootstrap_servers='localhost:9092',group_id = 'group1',auto_offset_reset='earliest')
training_data = CustomerBot.trainData(
                        "John's Shop", 
                        "123 Main St, Boston MA,USA",
                        "info@johns.shop",
                        "Customer focus, Quality, Integrity",
                        "To provide excellent products and service",
                        "2010",
                        "squirt guns, sandwiches, butane"
                    )
def send_to_kafka(data,consumer):

    producer.send('thisATest', data.encode())
    producer.flush()
    response = CustomerBot.openAI(CustomerBot,training_data,consumer)
    #send_ai_kafka(response)
    return response
def send_ai_kafka(message):
        producer =  KafkaProducer(bootstrap_servers=SERVER)
        producer.send('aiResponse',message.encode('utf-8'))



#user = input("What can I help you with today")
#print(send_to_kafka(user))





    



