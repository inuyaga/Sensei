from django import forms
from django.contrib.auth.forms import UserCreationForm
from aplicaciones.usuario.models import User

TIPO_USER = (
    (1, 'Maestro'),
    (2, 'Alumno'),
)
class UserForm(UserCreationForm):
    tipo_de_usuario = forms.ChoiceField(choices=TIPO_USER)
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
class UserFormEdit(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email', 'foto_perfil', 'acerca_de_mi', 'fecha_nacimiento', 'telefono')
        widgets= {
        'acerca_de_mi': forms.Textarea(attrs={'cols': 25, 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super(UserFormEdit, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})



