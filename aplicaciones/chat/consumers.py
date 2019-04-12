from channels.generic.websocket import AsyncWebsocketConsumer
import json
from aplicaciones.chat.models import Mensaje
from aplicaciones.usuario.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        nombre_completo = text_data_json['nombre_completo']
        usuario_envia = text_data_json['usuario_envia']
        foto_perf = text_data_json['foto_perf']

        grup_enviar = text_data_json['grup_enviar']

        if message == '' or message == None:
            pass
        else:
            emisor=User.objects.get(username=usuario_envia)
            receptor=User.objects.get(username=grup_enviar)
            msn=Mensaje(mensaje=message,mensaje_para=receptor,mensaje_de=emisor)
            msn.save()

        # Send message to room group
        await self.channel_layer.group_send(
            grup_enviar,
            {
                'type': 'chat_message',
                'message': message,
                'user': nombre_completo,
                'foto_perfil': foto_perf,
                'user_send': usuario_envia,
                'user_recibe': grup_enviar,
            }
        )

        await self.send(text_data=json.dumps({
            'message': message,
            'user': nombre_completo,
            'foto_perfil': foto_perf,
            'user_send': usuario_envia,
        }))

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        nombre_completo = event['user']
        usuario_envia = event['user_send']
        foto_perf = event['foto_perfil']
        user_recibe = event['user_recibe']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user': nombre_completo,
            'foto_perfil': foto_perf,
            'user_send': usuario_envia,
            'user_recibe': user_recibe,
        }))