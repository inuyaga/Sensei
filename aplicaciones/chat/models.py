from django.db import models
from django.contrib.auth import get_user_model
Usuario = get_user_model()
# Create your models here.
class Mensaje(models.Model):
    mensaje=models.TextField('Mensaje')
    mensaje_creado=models.DateTimeField('Creado',auto_now_add=True)
    grupo_name=models.CharField('Grupo', max_length=100, default='none')
    mensaje_para=models.ForeignKey(Usuario, verbose_name='para', related_name='user_destino', on_delete=models.CASCADE)
    mensaje_de=models.ForeignKey(Usuario, verbose_name='de',related_name='user_creado',  on_delete=models.CASCADE)
    STATUS=((1, 'Entregado'),(2, 'Visto'))
    mensaje_status=models.IntegerField("Estado", choices=STATUS, default=1)
    def __str__(self):
        return str(self.mensaje_creado)
