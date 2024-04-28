from django.db import models
from django.contrib.auth.models import User


# Create your models here.
"""
class Belegschaft(models.Model):
    name = models.CharField(max_length=50)
    vorname = models.CharField(max_length=50)
    strasse = models.CharField(max_length=50)
    plz = models.CharField(max_length=5)
    ort = models.CharField(max_length=50)

    def __str__(self):
        return self.name
"""


class Abteilungen(models.Model):
    numerischername = models.CharField(max_length=50)
    bezeichnung = models.CharField(max_length=50)
    personal = models.ManyToManyField(User, through='Personalzuordnung')

    def __str__(self):
        return self.numerischername

class Personalzuordnung(models.Model):
    mitarbeiter = models.ForeignKey(User, on_delete=models.CASCADE)
    abteilung = models.ForeignKey(Abteilungen, on_delete=models.CASCADE)
    seit = models.DateField()
    bis = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'MA: {self.mitarbeiter}| abt. {self.abteilung}'
    
class Abteilungsleiter(models.Model):
    abteilung = models.ForeignKey(Abteilungen,  on_delete=models.CASCADE)
    leiter = models.ForeignKey(User, verbose_name="Abteilungsleiter", on_delete=models.CASCADE)
    seit = models.DateField()
    bis = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Abt. {self.abteilung} | Leiter: {self.leiter}'


#Beurteilungstemplate

class Beurteilungstemplate(models.Model):
    beurteilungstemplate_bezeichnung = models.CharField(max_length=255 )

class Beurteilungsgliederung(models.Model):
    gliederung = models.CharField(max_length=50)
    beurteilungstemplate = models.ForeignKey(Beurteilungstemplate, on_delete=models.CASCADE)
    
class Beurteilungsauspraegungen(models.Model):
    beurteilungsausprägung = models.CharField(max_length=50)
    punktwert = models.IntegerField()

class Beurteilungsmerkmale(models.Model):
    beurteilungsmerkmal = models.CharField( max_length=50)
    untergruppe = models.ForeignKey(Beurteilungsgliederung, on_delete=models.CASCADE)
    beurteilungstemplate = models.ForeignKey(Beurteilungstemplate, on_delete=models.CASCADE)
    beurteilungsauspraegungen = models.ForeignKey(Beurteilungsauspraegungen, on_delete=models.CASCADE)

class Beurteilungsadressaten(models.Model):
    beurteilungstemplate = models.ForeignKey(Beurteilungstemplate, on_delete=models.CASCADE)



#Beurteilung

class Beurteilungen(models.Model):
    beurteilung_bez = models.CharField(max_length=255)
    beurteilung_erl = models.CharField(max_length=255)
    beurteilungstemplate = models.ForeignKey(Beurteilungstemplate, on_delete=models.CASCADE)
    erstbeurteiler = models.ForeignKey(User, on_delete=models.CASCADE, related_name='erstbeurteiler')
    zweitbeurteiler = models.ForeignKey(User, on_delete=models.CASCADE, related_name='zweitbeurteiler')
    beurteilter = models.ForeignKey(User, on_delete=models.CASCADE)
    frist_erstbeurteilung = models.DateField()
    frist_zweitbeurteilung = models.DateField()

    def __str__(self):
        return f'be: {self.beurteilung}| MA. {self.beurteilter}'

class Beurteilung_Beurteilungsmerkmale(models.Model):
    beurteilung = models.ForeignKey(Beurteilungen, on_delete=models.CASCADE)
    be_merkmal = models.ForeignKey(Beurteilungsmerkmale, on_delete=models.CASCADE)
    be_auspraegung = models.ForeignKey(Beurteilungsauspraegungen, on_delete=models.CASCADE)

    def __str__(self):
        return f'be: {self.beurteilung}| MA. {self.be_merkmal}'



