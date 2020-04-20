from django import forms
from aplicaciones.ctr_escolar.models import *
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
        'tarea_hora_init': forms.TimeInput(attrs={'type': 'time', 'step':'1'}),
        'tarea_hora_end' : forms.TimeInput(attrs={'type': 'time', 'step':'1'}),
        }


    def __init__(self, *args, **kwargs):
        super(TareaForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
class TareaFormEdit(forms.ModelForm):
    class Meta:
        model = Tarea
        exclude = ['tarea_unidad']
        widgets = {
        # 'tarea_fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
        # 'tarea_fecha_termino' : forms.DateInput(attrs={'type': 'date'}),
        'tarea_hora_init': forms.TimeInput(attrs={'type': 'time', 'step':'1'}),
        'tarea_hora_end' : forms.TimeInput(attrs={'type': 'time', 'step':'1'}),
        }
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
        # widgets = {
        # 'blog_materia': forms.CheckboxSelectMultiple(attrs={'type': 'checkbox'}),
        # }

    def __init__(self, *args, **kwargs):
        id_user = kwargs.pop('user')
        super(BlogFrom, self).__init__(*args, **kwargs)
        self.fields['blog_materia'].queryset=Materia.objects.filter(materia_aula__aula_pertenece=id_user)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        # self.fields['blog_materia'].widget.attrs.update({'class': 'form-check-input'})

class TareaDocumentoFrom(forms.ModelForm):
    class Meta:
        model = TareaDocumento
        fields = (
            'tareaDocumento_archivo',
            'tareaDocumento_comentario_alumno',
            )
        widgets = {
        'tareaDocumento_comentario_alumno': forms.Textarea(),
        }
    def __init__(self, *args, **kwargs):
        super(TareaDocumentoFrom, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

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


# class ExamenForm(forms.ModelForm):
#     # ex_hora_init = forms.TimeField(label="Hora inicial", help_text="Formato de 24hrs H:M:S.")
#     # ex_hora_end = forms.TimeField(label="Hora Final", help_text="Formato de 24hrs H:M:S.")
#     class Meta:
#         model = Examen
#         fields = ('__all__')
#         widgets = {
#         'ex_hora_init': forms.TimeInput(attrs={'type': 'time', 'step':'1'}),
#         'ex_hora_end' : forms.TimeInput(attrs={'type': 'time', 'step':'1'}),
#         }
    
#     def __init__(self, *args, **kwargs):
#         super(ExamenForm, self).__init__(*args, **kwargs)
#         # self.fields['materia_aula'].queryset=Aula.objects.filter(aula_pertenece=id_user)
#         for field in self.fields:
#             self.fields[field].widget.attrs.update({'class': 'form-control'})


class ReactivoForm(forms.ModelForm):
    class Meta:
        model = Reactivo
        fields = ('__all__')
    
    def __init__(self, *args, **kwargs):
        super(ReactivoForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        
        self.fields['rec_nombre'].widget.attrs.update({'v-model': 'question_text'})
        self.fields['rec_tipo'].widget.attrs.update({'@change': 'onChange($event)'})



