import asyncio
import json
from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async
from django.conf import settings
import logging
import threading
import time
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from scripts.main import getData
class CustomConsumer(AsyncJsonWebsocketConsumer):
    async def websocket_connect(self,event):
        print("****************************************")
        print("connected",event)
        print("****************************************")
        self.rooms = set()
        await self.channel_layer.group_add(
            "hello",
            self.channel_name,
        )
        await self.accept()
        
        # await self.channel_layer.group_send(
        #     "hello",
        #     {
        #         "type": "data",
        #         "message":"hello"
        #     }
        # )

    async def websocket_receive(self,event):
        
        print("receive",event)


    async def websocket_disconnect(self,event):
        print("****************************************")
        print("disconnected",event)
        print("****************************************")
    
    async def chat_message(self, event):
        """
        Called when someone has messaged our chat.
        """
        # Send a message down to the client
        await self.send_json(
            {
                "msg_type": settings.MSG_TYPE_MESSAGE,
                "room": "hello",
                "message": event["message"],
            },
        )

class PositionConsumer(AsyncJsonWebsocketConsumer):
    async def websocket_connect(self,event):
        self.rooms = set()
        await self.channel_layer.group_add(
            "position",
            self.channel_name,
        )
        await self.accept()


    async def websocket_receive(self,event):
        
        print("receive",event)


    async def websocket_disconnect(self,event):
        print("****************************************")
        print("disconnected",event)
        print("****************************************")
    
    async def chat_message(self, event):
        """
        Called when someone has messaged our chat.
        """
        # Send a message down to the client
        await self.send_json(
            {
                "msg_type": settings.MSG_TYPE_MESSAGE,
                "room": "hello",
                "message": event["message"],
            },
        )

def func():
    while True:
        print("hmm")
        message = getData("/order")
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "hello",
            {
                "type": "chat.message",
                "message": message,
            }

        )
        
        time.sleep(2)


