"""."""
import json
import datetime
from channels.generic.websocket import AsyncWebsocketConsumer


class Chat(AsyncWebsocketConsumer):
    """."""

    async def connect(self):
        """."""
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        """."""
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        """."""
        text_data = json.loads(text_data)

        name = text_data["name"]
        message = text_data["message"]

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "name": name,
                "message": message
            }
        )

    async def chat_message(self, event):
        """."""
        name = event["name"]
        message = event["message"]

        time = datetime.datetime.now()
        time = time.strftime("%d %b %Y %H:%M")

        await self.send(text_data=json.dumps({
            "name": name,
            "time": time,
            "message": message
        }))
