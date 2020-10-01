from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken

from aplicaciones.ctr_escolar.models import *
from aplicaciones.apirest.serializers import *
from rest_framework.authtoken.models import Token
import json

# class GetAulaMaestro(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
        
#     def get(self, request):
#         alula = Aula.objects.filter(aula_pertenece=self.request.user)
#         content = {
#             'nombre': alula.aula_nombre,
#             'creado': alula.aula_creacion,
#             }
#         return Response(content)



class GetAulaMaestro(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(aula_pertenece=self.request.user)
        return queryset


class DeleteAulaMaestro(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer
    lookup_field = 'id'


class MateriasMateriasView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny] 
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(materia_aula__aula_pertenece=self.request.user, materia_aula=self.kwargs.get('idaula'))
        
        return queryset


class AutenticacionUser(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)        
        data = {
            'token': token.key,             
            'username':str(user.username),
            'nombre':str(user.get_full_name)
        }
        return Response(data)