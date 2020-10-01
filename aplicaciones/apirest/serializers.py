from rest_framework import serializers
from django.utils.formats import localize
from aplicaciones.ctr_escolar.models import Aula, Materia

class AulaSerializer(serializers.HyperlinkedModelSerializer):
    aula_creacion = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%Shrs')
    class Meta:
        model = Aula
        fields = ['id', 'aula_nombre',  'aula_creacion']
class MateriaSerializer(serializers.ModelSerializer):
    materia_creado = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%Shrs')
    class Meta:
        model = Materia
        fields = ['materia_id', 'materia_aula',  'materia_nombre','materia_creado']
        # read_only_fields = ('id',)