# Generated by Django 2.2 on 2019-08-11 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctr_escolar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='materia_archivos',
            field=models.ManyToManyField(blank=True, null=True, to='ctr_escolar.Documento', verbose_name='Archivos'),
        ),
    ]
