from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import spacy
# from spacy.cli.download import download
# spacy.load('en_core_web_sm')
# download(model="en_core_web_sm")

import en_core_web_sm
nlp = spacy.load("en_core_web_sm")

chatbot=ChatBot('Crazy ChatBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")



class ChatConsumer(WebsocketConsumer):


	def connect(self):
		self.room_name = self.scope['url_route']['kwargs']['room_name']
		self.room_group_name = 'chat_%s' % self.room_name
		async_to_sync(self.channel_layer.group_add)(
			self.room_group_name,
			self.channel_name
			)
		self.accept()
		self.send(text_data=json.dumps({'status':'connected'}))

	def receive(self, text_data):
		print(text_data)
		# self.send(text_data=json.dumps({'message':text_data}))
		text_data_json = json.loads(text_data)
		message = text_data_json['message']
		sender = text_data_json['sender']
		chat_type = text_data_json['chat_type']
		data = {"chat_type":chat_type, "sender":sender ,"message":message}


		async_to_sync(self.channel_layer.group_send)(
			self.room_group_name,
			{
				'type': 'chat_message',
				'message': data
			}
		)


	def disconnect(self, *args, **kwargs):
		print("disconnected")
		
	def send_notification(self, event):
		data = event.get("value")
		self.send(text_data = json.dumps({'payload':data}))

	def chatboat_message(self, message):
		message = message['message']

		response = chatbot.get_response(message)
		data = {"message":str(response)}

		# Send message to WebSocket
		self.send(text_data=json.dumps({
			"sender" : "Crazy Asistant",
			"message": data
		}))

	def chat_message(self, event):
		print(f'47-----------{event}')
		data = event['message']
		sender = data['sender']
		message = data['message']
		chat_type = data['chat_type']


		# Send message to WebSocket
		self.send(text_data=json.dumps({
			"sender" : sender,
			"message": message
		}))
		if chat_type == "chatbot":
			self.chatboat_message({"message":message})
