from django import forms
from aplicaciones.ctr_escolar.models import Aula, Materia, Documento, Unidad, Tarea, Blog, \
TareaDocumento, ComentarioBlog
from django.forms.widgets import CheckboxSelectMultiple
from ajax_select.fields import AutoCompleteSelectMultipleField
class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        exclude = ['aula_pertenece']
    def __init__(self, *args, **kwargs):
        super(AulaForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = '__all__'
        widgets = {
        'materia_archivos': forms.CheckboxSelectMultiple(attrs={'type': 'checkbox'}),
        }
    materia_archivos = AutoCompleteSelectMultipleField('documentos_tags',required=False, help_text='Escriba el nombre del documento a agregar, y seleccione.')
    materia_registro_alumnnos = AutoCompleteSelectMultipleField('user_register_materia',label='Alumnos registrados', required=False, help_text='Escriba el nombre de usuario del alumno.')
    
    def __init__(self, *args, **kwargs):
        id_user = kwargs.pop('user')
        super(MateriaForm, self).__init__(*args, **kwargs)
        self.fields['materia_aula'].queryset=Aula.objects.filter(aula_pertenece=id_user)
        # self.fields['materia_archivos'].queryset=Documento.objects.filter(doc_pertenece=id_user)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        # self.fields['materia_archivos'].widget.attrs.update({'class': 'form-check-input'})

class MateriaFormEdit(forms.ModelForm):
    class Meta:
        model = Materia
        fields = '__all__'
        widgets = {
        'materia_archivos': forms.CheckboxSelectMultiple(attrs={'type': 'checkbox'}),
        }
    materia_archivos = AutoCompleteSelectMultipleField('documentos_tags',required=False, help_text='Escriba el nombre del documento a agregar, y seleccione.')
    materia_registro_alumnnos = AutoCompleteSelectMultipleField('user_register_materia',label='Alumnos registrados',required=False, help_text='Escriba el nombre de usuario del alumno.')

    def __init__(self, *args, **kwargs):
        id_user = kwargs.pop('user')
        super(MateriaFormEdit, self).__init__(*args, **kwargs)
        self.fields['materia_aula'].queryset=Aula.objects.filter(aula_pertenece=id_user)
        # self.fields['materia_archivos'].queryset=Documento.objects.filter(doc_pertenece=id_user)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        # self.fields['materia_archivos'].widget.attrs.update({'class': 'form-check-input'})

class DocumentoCreateForm(forms.ModelForm):
    class Meta:
        model = Documento
        exclude = ['doc_pertenece']

    def __init__(self, *args, **kwargs):
        id_user = kwargs.pop('user')
        super(DocumentoCreateForm, self).__init__(*args, **kwargs)
        # self.fields['doc_pertenece'].queryset=Documento.objects.filter(doc_pertenece=id_user)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class UnidadForm(forms.ModelForm):
    class Meta:
        model = Unidad
        fields = ('unidad_nombre',)


    def __init__(self, *args, **kwargs):
        # id_user = kwargs.pop('user')
        super(UnidadForm, self).__init__(*args, **kwargs)
        # self.fields['materia_aula'].queryset=Aula.objects.filter(aula_pertenece=id_user)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

        # self.fields['unidad_materia'].widget.attrs.update({'class': 'invisible'})
class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        # fields = ('__all__')
        exclude = ['tarea_unidad']
        widgets = {
        'tarea_fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
        'tarea_fecha_termino' : forms.DateInput(attrs={'type': 'date'}),
        }


    def __init__(self, *args, **kwargs):
        super(TareaForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
class TareaFormEdit(forms.ModelForm):
    class Meta:
        model = Tarea
        exclude = ['tarea_unidad']
    def __init__(self, *args, **kwargs):
        super(TareaFormEdit, self).__init__(*args, **kwargs)
        # self.fields['materia_aula'].queryset=Aula.objects.filter(aula_pertenece=id_user)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
class BlogFrom(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            'blog_titulo',
            'blog_descripcion',
            'blog_imagen',
            'blog_materia',
            'blog_contenido',
            )
        widgets = {
        'blog_materia': forms.CheckboxSelectMultiple(attrs={'type': 'checkbox'}),
        }

    def __init__(self, *args, **kwargs):
        id_user = kwargs.pop('user')
        super(BlogFrom, self).__init__(*args, **kwargs)
        self.fields['blog_materia'].queryset=Materia.objects.filter(materia_aula__aula_pertenece=id_user)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['blog_materia'].widget.attrs.update({'class': 'form-check-input'})

class TareaDocumentoFrom(forms.ModelForm):
    class Meta:
        model = TareaDocumento
        exclude = ['blog_pertenece',
        'tareaDocumento_comentario_maestro',
        'tareaDocumento_pertenece',
        'tareaDocumento_calificacion',
        'tareaDocumento_status',
        'tareaDocumento_tipo',
        ]
        widgets = {
        'tareaDocumento_comentario_alumno': forms.Textarea(),
        }
    def __init__(self, *args, **kwargs):
        id_user = kwargs.pop('user')
        super(TareaDocumentoFrom, self).__init__(*args, **kwargs)
        self.fields['tareaDocumento_Tarea'].queryset=Tarea.objects.filter(tarea_unidad__unidad_materia__materia_registro_alumnnos=id_user)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['tareaDocumento_Tarea'].widget.attrs.update({'class': 'invisible'})
        self.fields['tareaDocumento_Tarea'].label = ''

class TareaEntregadaEdit(forms.ModelForm):
    class Meta:
        model = TareaDocumento
        exclude = ['tareaDocumento_archivo','tareaDocumento_comentario_alumno','tareaDocumento_pertenece','tareaDocumento_Tarea','tareaDocumento_status']
    def __init__(self, *args, **kwargs):
        super(TareaEntregadaEdit, self).__init__(*args, **kwargs)
        # self.fields['materia_aula'].queryset=Aula.objects.filter(aula_pertenece=id_user)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
class ComentarioBlogForm(forms.ModelForm):
    class Meta:
        model = ComentarioBlog
        exclude = ['comentario_blog','comentario_comentado_by']
    def __init__(self, *args, **kwargs):
        super(ComentarioBlogForm, self).__init__(*args, **kwargs)
        # self.fields['materia_aula'].queryset=Aula.objects.filter(aula_pertenece=id_user)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})



