from django.contrib import admin

from locales import models

admin.site.register(models.UserProfile)
admin.site.register(models.Empresas)
admin.site.register(models.ClasificacionesEmpresas)
admin.site.register(models.MedidasSanitarias)
