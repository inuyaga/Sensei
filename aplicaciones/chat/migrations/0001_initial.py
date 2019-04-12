# Generated by Django 2.1.7 on 2019-04-03 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
                ('mensaje_creado', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('grupo_name', models.CharField(default='none', max_length=100, verbose_name='Grupo')),
                ('mensaje_de', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_creado', to=settings.AUTH_USER_MODEL, verbose_name='de')),
                ('mensaje_para', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_destino', to=settings.AUTH_USER_MODEL, verbose_name='para')),
            ],
        ),
    ]