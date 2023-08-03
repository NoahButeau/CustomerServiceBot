#this is a filler for the website 
from PyQt6 import QtWidgets
from kafkaUtils import send_to_kafka
from kafka import KafkaConsumer
consumer = KafkaConsumer('thisATest',bootstrap_servers='localhost:9092',group_id = 'group1',auto_offset_reset='earliest')

class ChatBot(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        self.text_area = QtWidgets.QTextBrowser()  
        
        self.input_line = QtWidgets.QLineEdit()          
        
        self.send_button = QtWidgets.QPushButton("Send")              
        self.send_button.clicked.connect(self.send)
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.text_area)     
        layout.addWidget(self.input_line) 
        layout.addWidget(self.send_button)  
        self.setLayout(layout)           
        
    def send(self):
    
        message = self.input_line.text()

        self.input_line.setText("") 
        response = send_to_kafka(message,consumer) 

        
        
        
        self.text_area.append("User: " + message)
        self.text_area.append("Chatbot: " + response)
app = QtWidgets.QApplication([])
chat_window = ChatBot()
chat_window.show()
app.exec()