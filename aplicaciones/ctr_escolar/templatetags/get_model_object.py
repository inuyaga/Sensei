from django import template
from aplicaciones.ctr_escolar.models import Unidad
register = template.Library()

@register.filter
def unidades_materia(id_materia):
    unidades=Unidad.objects.filter(unidad_materia=id_materia)
    return unidades