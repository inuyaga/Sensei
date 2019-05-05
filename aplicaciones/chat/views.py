from django.shortcuts import render
from django.views.generic import TemplateView
from aplicaciones.chat.models import Mensaje
from aplicaciones.usuario.models import User
from django.db.models import Q
from django.http import JsonResponse
# Create your views here.
class ChatIndex(TemplateView):
    template_name='chat/chat_index.html'
    def get_context_data(self, **kwargs):
        from django.utils.safestring import mark_safe
        import json
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user


        context['maestro'] = self.request.user.is_maestro
        context['alumno'] = self.request.user.is_alumno
        context['foto_perfil'] = self.request.user.foto_perfil
        context['Usuario'] = self.request.user
        context['activate'] = 'Chat'

        conversaciones=set()
        conversacionesF=[]
        msn = Mensaje.objects.filter(Q(mensaje_para=self.request.user) | Q(mensaje_de=self.request.user))
        for historial in msn:
            conversaciones.add(historial.mensaje_para)
            conversaciones.add(historial.mensaje_de)
            print(historial.mensaje_creado)
        conversaciones.discard(self.request.user)

        for busqueda in conversaciones:
            conversacionesF.append({'usr':busqueda, 'no_leido':Mensaje.objects.filter(mensaje_para=self.request.user,mensaje_de=busqueda, mensaje_status=1).count()})

        context['list_usuarios'] = conversacionesF
        context['list_usr_serach'] = User.objects.exclude(username=self.request.user)



        return context

class ChatSelected(TemplateView):
    template_name='chat/seled_master.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['maestro'] = self.request.user.is_maestro
        context['alumno'] = self.request.user.is_alumno
        context['foto_perfil'] = self.request.user.foto_perfil
        context['Usuario'] = self.request.user
        context['activate'] = 'Chat'
        context['maestro_list'] = User.objects.filter(is_maestro=True)


        return context

class RetornaUsuario(TemplateView):
    template_name='chat/seled_master.html'

    def post(self, request, *args, **kwargs):
        data =  dict()
        query=User.objects.get(username=request.POST.get('usr'))
        data['user']=str(query.username)
        data['nombre']=str(query.get_full_name())
        data['foto']=str(query.foto_perfil)
        return JsonResponse(data)

class HistoricoConversacion(TemplateView):
    template_name='chat/seled_master.html'

    def post(self, request, *args, **kwargs):

        usr_seleccionado=request.POST.get('usr_seleccionado')
        usr_princ=request.POST.get('usr_princ')

        data =  dict()
        query=Mensaje.objects.filter(Q(mensaje_para__username=usr_princ) | Q(mensaje_de__username=usr_princ))
        data['historia']=list(query.filter(Q(mensaje_para__username=usr_seleccionado) | Q(mensaje_de__username=usr_seleccionado)).values('mensaje','mensaje_creado','mensaje_para','mensaje_de').order_by('mensaje_creado'))

        return JsonResponse(data)

class MarcarMensajes(TemplateView):
    template_name='chat/seled_master.html'

    def post(self, request, *args, **kwargs):

        emisor=request.POST.get('emisor')
        Mensaje.objects.filter(mensaje_para=self.request.user,mensaje_de__username=emisor).update(mensaje_status=2)
        data=dict()
        data['actualizado']=True

        return JsonResponse(data)

class Firebase(TemplateView):
    template_name = 'chat/chat_firebase.html'
