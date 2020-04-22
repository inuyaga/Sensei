from django import template
from aplicaciones.ctr_escolar.models import Tarea, EleccionReactivo
register = template.Library()
from django.utils import timezone
from django.urls import reverse_lazy
from datetime import datetime
@register.filter
def is_aviable_tarea(id_tarea):
    ahora = timezone.now().date()
    obj_tarea = Tarea.objects.get(tarea_id=id_tarea)
    fecha_inicial = obj_tarea.tarea_fecha_inicio
    fecha_final = obj_tarea.tarea_fecha_termino

    if fecha_inicial <= ahora <= fecha_final:
        return True
    else:
        return False

@register.filter
def is_mark_reactivo_true(id_reactivo):
    reactivo = EleccionReactivo.objects.filter(el_reactivo=id_reactivo, el_verdadero=True).count()
    print(reactivo)
    if reactivo >= 1:
        return 'success'
    else:
        return 'primary'

@register.filter
def return_button_tarea(id_tarea):
    obj_tarea = Tarea.objects.get(tarea_id=id_tarea)
    
    if obj_tarea.tarea_tipo == 'ENTREGA':
        url = reverse_lazy('ctr:al_tareas_create', kwargs={'id_unidad':obj_tarea.tarea_unidad.unidad_id, 'id_tarea':id_tarea})
        html =""" 
            <a href="{}" class="btn btn-sm btn-labeled btn-success">
                <span class="btn-label">
                    <span class="oi oi-book" aria-hidden="true"></span>
                </span>
                <span class="btn-text">
                    Entregar
                </span>
            </a>
            """.format(url)
        return html


    if obj_tarea.tarea_tipo == 'PARA CALIFICAR':
        html ="""<span class="badge badge-info">No es necesario entregar</span>"""
        return html

        
    if obj_tarea.tarea_tipo == 'EXAMEN':
        ahora = datetime.now().time()
        ahora_inicial = obj_tarea.tarea_hora_init
        ahora_final = obj_tarea.tarea_hora_end
        if ahora_inicial <= ahora <= ahora_final:
            html =""" 
                <a href="{}" class="btn btn-sm btn-labeled btn-success">
                    <span class="btn-label">
                        <span class="oi oi-book" aria-hidden="true"></span>
                    </span>
                    <span class="btn-text">
                        Responder
                    </span>
                </a>
                """.format(reverse_lazy('ctr:al_examen', kwargs={'id_examen':id_tarea}))
            return html
        else:
            return """<span class="badge badge-info">inicia:{} - termina:{}</span>""".format(ahora_inicial, ahora_final)

        
    




