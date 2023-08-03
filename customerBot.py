from urllib import request
import openai
import json
from kafka import KafkaProducer
from kafka import KafkaConsumer
import time


SERVER = 'localhost:9092'
class CustomerBot:       
    def openAI(self,training_data,consumer):
        openai.api_key = KEY
        #consumer = KafkaConsumer('thisATest',bootstrap_servers=SERVER,group_id = 'group1',auto_offset_reset='latest')

        for message in consumer:
            print("made it here")
            print(f'Received message: {message.value.decode("utf-8")}')
            question = message.value.decode("utf-8")
            consumer.commit()
            break
            
                
        response = openai.Completion.create(
            engine='text-davinci-002',
            prompt=f"{training_data} Q: {question}\nA:",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5
        )
        #response = 'what time does the store open'
        
        
        response_json = json.dumps(response)
        response_dict = json.loads(response_json)
        newResponse= response_dict['choices'][0]['text']
        return newResponse
        return question
        

    def trainData(buisness,address,email,core,mission,founded,products):
        training_data = f"""
        Q: What are your business hours? A: We are open Monday through Friday from 9am to 5pm.
        Q: Do you offer free shipping? A: Yes! For orders over $50, we offer free standard shipping.
        Q: What is your return policy? A: We offer a 30-day return policy for unworn and undamaged items.
        Q: How can I contact customer support? A: You can contact our customer support team at support@{buisness}.com or 1-800-555-5555.
        Q: What payment methods do you accept? A: We accept Visa, Mastercard, American Express, Discover, Apple Pay and Google Pay.
        Q: How secure is my information? A: We use industry-standard encryption to ensure all customer data is secure and protected.
        Q: Do you offer any discounts? A: We offer 15% off for students, teachers and seniors. Check our website for seasonal discount codes.
        Q: When will my order arrive? A: Most orders arrive within 3 to 5 business days after shipping. Some remote locations may take longer.
        Q: Can I track my order? A: Yes! Once shipped, you'll receive a tracking number to follow the progress of your package.
        Q: How do I change or cancel my order? A: Please contact our customer support team and we'll be happy to assist you with any order changes.
        Q: Do you offer after purchase support? A: Yes, our customer service team is available to help with anything regarding your order after purchase.
        Q: What payment methods do you accept? A: We accept all major credit cards, PayPal, Apple Pay, Google Pay and even mail-in checks.
        Q: Do you sell gift cards? A: Yes! You can purchase eGift cards or physical gift cards for any denomination on our website.
        Q: What is your shipping policy for international orders? A: We ship worldwide but additional shipping fees and customs charges may apply.
        Q: How do I contact you if there is an issue with my order? A: Please email us at {email} with your order number and full details of the issue and we'll assist you.
        Q: Do you offer assembly or installation services? A: Unfortunately we do not offer assembly or installation services directly but can refer you to qualified providers.
        Q: What is your mailing address? A: {buisness} {address} 
        Q: How do I change the shipping address on my order? A: Please contact our customer support team via phone or email and we'll be happy to update the shipping address for you.
        Q: Do you sell vintage or pre-owned items? A: No, we only sell new items directly from the manufacturer.
        Q: What is the refund process if I return an item? A: Once we receive your return, we will issue a full refund to your original payment method within 3-5 business days.
        Q: Do you sell wholesale? A: Yes! Please contact us at {email} for wholesale account setup and pricing.
        Q: How do I report a broken or defective product? A: Please contact our customer support team with your order number and details about the issue. We'll assist you from there.
        Q: Do you provide assembly instructions or manuals? A: Yes! Assembly instructions and product manuals are included with all items where applicable.
        Q: What is the origin of the products you sell? A: Our products are sourced from a variety of manufacturers located in USA.
        Q: How long have you been in business? A: We have been operating for a number of years, since {founded}.
        Q: What payment options are available for international orders? A: For international orders, we accept payment via major credit cards and PayPal.
        Q: Do you have a loyalty program or rewards? A: Currently we do not have a loyalty program, but we look forward to implementing rewards for our valued customers in the future.
        Q: What is your company's mission or core values? A: Our mission is {mission}. Our core values are {core}.
        Q: Do you test all products for safety and quality? A: Yes, all products undergo rigorous quality testing before being made available for sale.
        Q: What kind of products do you offer? A: We offer {products}
        """
        return training_data
