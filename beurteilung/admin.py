from django.contrib import admin
from .models import Abteilungen, Abteilungsleiter, Beurteilungsmerkmale, Beurteilungen, Beurteilung_Beurteilungsmerkmale, Beurteilungsadressaten, Beurteilungsauspraegungen, Beurteilungsgliederung, Beurteilungstemplate, Personalzuordnung, Addresatentemplate, User_Addresatentemplate_zuordnung, Beurteilungstemplate_Beurteiler, Beurteilung_beurteiler, Beurteilungstemplate_Beurteiler   

# Register your models here.

admin.site.register(Abteilungen)
admin.site.register(Abteilungsleiter)
admin.site.register(Beurteilung_Beurteilungsmerkmale)
admin.site.register(Beurteilungen)
admin.site.register(Beurteilung_beurteiler)
admin.site.register(Beurteilungstemplate_Beurteiler)
admin.site.register(Beurteilungsadressaten)
admin.site.register(Beurteilungsauspraegungen)
admin.site.register(Beurteilungsgliederung)
admin.site.register(Beurteilungstemplate)
admin.site.register(Personalzuordnung)
admin.site.register(Beurteilungsmerkmale)
admin.site.register(Addresatentemplate)
admin.site.register(User_Addresatentemplate_zuordnung)
