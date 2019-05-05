from django.urls import path
from aplicaciones.chat import views as ViewChat
app_name='chat'
urlpatterns = [
    path('Chat/',ViewChat.ChatIndex.as_view(), name='index'),
    path('get_usr/chat/',ViewChat.RetornaUsuario.as_view(), name='get_user'),
    path('get_usr/chat/historico/',ViewChat.HistoricoConversacion.as_view(), name='get_user_historia'),
    path('mensaje/chat/historico/marcar_leido/',ViewChat.MarcarMensajes.as_view(), name='marcar_msn'),
    path('mensaje/firebase/',ViewChat.Firebase.as_view(), name='firebase'),

    # path('chat_rom',ViewChat.ChatSelected.as_view(), name='rom'),
] 