from django import template
from aplicaciones.ctr_escolar.models import Unidad, EleccionReactivo
register = template.Library()

@register.filter
def unidades_materia(id_materia):
    unidades=Unidad.objects.filter(unidad_materia=id_materia)
    return unidades

@register.filter
def elecciones_reactivo(id_reactivo):
    elecciones=EleccionReactivo.objects.filter(el_reactivo=id_reactivo)
    return elecciones