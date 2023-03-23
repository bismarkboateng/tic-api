import json 
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocktConsumer


class TextRoomConsumer(WebsocktConsumer):

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()


    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )


    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        text = text_data_json["text"]
        sender = text_data_json["sender"]

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": text,
                "sender": sender
            }
        )

    def chat_message(self, event):
        text = event["message"]
        sender = event["sender"]

        self.send(text_data=json.dumps({
            "text": text,
            "sender": sender
        }))