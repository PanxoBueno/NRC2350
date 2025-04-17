from django.contrib import admin
from .models import Atleta, Entrenador, Biblioteca
# Register your models here. aca se registran los modelos para ser CRUD en perfil admin

admin.site.register(Atleta)
admin.site.register(Entrenador)
admin.site.register(Biblioteca)