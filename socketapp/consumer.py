import asyncio
import json
from channels.consumer import AsyncConsumer
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async

class CustomConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print("****************************************")
        print("connected",event)
        print("****************************************")
        await self.send({
            "type":"websocket.accept"
        })

    async def websocket_receive(self,event):
        
        print("receive",event)

    async def websocket_disconnect(self,event):
        print("****************************************")
        print("disconnected",event)
        print("****************************************")
    