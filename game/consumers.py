import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class LobbyConsumer(WebsocketConsumer):
    def connect(self):
        self.party_id = self.scope['url_route']['kwargs']['party_id']
        
        async_to_sync(self.channel_layer.group_add)(
            self.party_id,
            self.channel_name
        )
        
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        async_to_sync(self.channel_layer.group_send)(
            self.party_id,
            {
                'type': 'button_clicked',
                'message': ''
            }
        )
    
    def button_clicked(self, event):
        self.send(text_data=json.dumps({
            'message': ''
        }))
