import re
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
import json
from account.models import User

class PrivateChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('Connect', event)
        user = self.scope['user']
        print(f'1->{user}')
        chat_room = f'user_chatroom_{user.id}'
        self.chat_room = chat_room
        print(f'->>>{self.channel_name}')
        await self.channel_layer.group_add(
            chat_room,
            self.channel_name
        )
        await self.send({
            'type' : 'websocket.accept'
        })

    
    async def websocket_receive(self, event):
        print('connected', event)
        received_data = json.loads(event['text'])
        msg = received_data.get('message')
        sent_by_id = received_data.get('sent_by')
        send_to_id = received_data.get('send_to')
        if not msg:
            print("Error :: empty message")
            return False
        
        sent_by_user = await self.get_user_object(sent_by_id)
        send_to_user = await self.get_user_object(send_to_id)

        if not sent_by_user:
            print("Error:: sent by user incorrect")
        
        if not send_to_user:
            print("Error:: send to user is incorrect")
        
        other_user_chat_room = f'user_chatroom_{send_to_id}'
        self_user = self.scope['user']
        print(f'2->{self_user}')
        response = {
            'message' : msg,
            'sent_by' : self_user.id,
        }

        await self.channel_layer.group_send(
            other_user_chat_room,
            {
                'type' : 'chat_message',
                'text' : json.dumps(response)
            }
        )


        await self.channel_layer.group_send(
            self.chat_room,
            {
                'type' : 'chat_message',
                'text' : json.dumps(response)
            }
        )

        # await self.send({
        #     'type' : 'websocket.send',
        #     'text' : json.dumps(response)
        # })

    
    async def websocket_disconnect(self, event):
        print('disconnected', event)

    async def chat_message(self, event):
        print('chat_message', event)

        await self.send({
            'type' : 'websocket.send',
            'text' : event['text']
        })

    @database_sync_to_async
    def get_user_object(self, user_id):
        qs = User.objects.filter(id=user_id)
        if qs.exists():
            obj = qs.first()
        else:
            obj = None
        return obj


