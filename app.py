from flask import Flask, request, render_template_string,render_template
from kafka import KafkaConsumer
from kafkaUtils import *
from customerBot import CustomerBot
from threading import Thread

app = Flask(__name__)
SERVER = 'localhost:9092'

'''
Idea is start the consumer to be constanly listening instead of calling the consumer once the entry is in there
consumer = KafkaConsumer('thisATest',bootstrap_servers=SERVER)
@app.route('/api/data', methods=['GET'])
def start_consumer():
    consumer = KafkaConsumer('thisATest',bootstrap_servers=SERVER,group_id = 'group1',auto_offset_reset='latest')
        while True:
            records = consumer.poll(timeout_ms=0)
            if records:
                for message in consumer:
                    print("made it here")
                    print(f'Received message: {message.value.decode("utf-8")}')
                    question = message.value.decode("utf-8")
                    consumer.commit()
                    break
                break
'''


@app.route('/api/data', methods=['GET','POST'])
def post_data():
    
    index = '<form method="post"><input name="text" type="text"><button type="submit">Submit</button></form>{% if text %}<p>Customer Service: {{ text }}</p>{% endif %}'
    if request.method == "POST":   
        print(request.form["text"])
        text = send_to_kafka(request.form["text"])
        return render_template_string(index,text=text)
    return render_template_string(index)

@app.route('/')        
def index():
    return render_template_string()


if __name__ == '__main__':
    app.run(debug=True)
    
