from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    is_alumno = models.BooleanField(default=False)
    is_maestro = models.BooleanField(default=False)
    foto_perfil=models.ImageField('Foto Perfil', upload_to='foto_perfil/')
    fecha_nacimiento=models.DateField('Fecha de nacimiento',null=True, blank=True)
    telefono=models.BigIntegerField('Telefono', null=True, blank=True)
    acerca_de_mi=models.CharField('Acerca de mi', max_length=1000, default='.....')
    # def __str__(self):
    #     return self.get_full_name()
    class Meta:
        db_table = 'auth_user' 
# Create your models here.
