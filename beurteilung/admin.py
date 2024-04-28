from django.contrib import admin
from .models import Abteilungen, Abteilungsleiter, Beurteilungsmerkmale, Beurteilungen, Beurteilung_Beurteilungsmerkmale, Beurteilungsadressaten, Beurteilungsauspraegungen, Beurteilungsgliederung, Beurteilungstemplate, Personalzuordnung

# Register your models here.

admin.site.register(Abteilungen)
admin.site.register(Abteilungsleiter)
admin.site.register(Beurteilung_Beurteilungsmerkmale)
admin.site.register(Beurteilungen)
admin.site.register(Beurteilungsadressaten)
admin.site.register(Beurteilungsauspraegungen)
admin.site.register(Beurteilungsgliederung)
admin.site.register(Beurteilungstemplate)
admin.site.register(Personalzuordnung)
admin.site.register(Beurteilungsmerkmale)
