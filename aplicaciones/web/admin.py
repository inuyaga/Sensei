from django.contrib import admin
from aplicaciones.web.models import Blog, Categoria, Tag
from tinymce.widgets import TinyMCE

from django import forms

class BlogForms(forms.ModelForm):
    blog_contenido = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Blog
        fields = ('__all__')

class BlogConfig(admin.ModelAdmin):
    form = BlogForms

# Register your models here.
admin.site.register(Blog, BlogConfig)
admin.site.register(Categoria)
admin.site.register(Tag)