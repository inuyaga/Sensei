from ajax_select import register, LookupChannel
from aplicaciones.ctr_escolar.models import Documento

@register('documentos_tags')
class TagsLookupDocumentos(LookupChannel):

    model = Documento

    def get_query(self, q, request):
        return self.model.objects.filter(doc_pertenece=request.user,doc_nombre__icontains=q).order_by('doc_nombre')[:50]

    def format_item_display(self, item):
        filtering='<span class="badge badge-pill badge-info">{}</span>'.format(item.doc_nombre)
        return filtering

