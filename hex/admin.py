from django.contrib import admin

from .models import People, Avaliador, Equipe, Empresa

admin.site.register(People)
admin.site.register(Avaliador)
admin.site.register(Equipe)
admin.site.register(Empresa)