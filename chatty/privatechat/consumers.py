from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
import json

class PrivateChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('Connect', event)
        await self.send({
            'type' : 'websocket.accept'
        })

    
    async def websocket_receive(self, event):
        print('connected', event)
        received_data = json.loads(event['text'])
        msg = received_data.get('message')
        if not msg:
            return False
        response = {
            'message' : msg
        }
        await self.send({
            'type' : 'websocket.send',
            'text' : json.dumps(response)
        })

    
    async def websocket_disconnect(self, event):
        print('disconnected', event)



