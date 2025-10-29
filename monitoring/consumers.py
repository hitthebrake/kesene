import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MonitorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if self.scope["user"].is_anonymous:
            await self.close()
            return
        await self.channel_layer.group_add("monitor", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("monitor", self.channel_name)

    async def send_measurement(self, event):
        # Send data to WebSocket
        await self.send(text_data=json.dumps(event["data"]))


class ScenarioConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if self.scope["user"].is_anonymous:
            await self.close()
            return
        await self.channel_layer.group_add("scenario", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("scenario", self.channel_name)

    async def send_scenarios(self, event):
        # Send data to WebSocket
        await self.send(text_data=json.dumps({
            'scenarios': event['scenarios'],
            'resolved_scenarios': event['resolved_scenarios'],
        }))
