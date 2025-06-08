from django.db import models
from django.contrib.auth.models import User



# Belegschaftsmanagement
class Abteilungen(models.Model):
    """
    Das Modell für die Abteilungen
    Die Organisationseinheit wird über die Tabelle Personalzuordnung mit dem User verknüpft"""

    numerischername = models.CharField(max_length=50)
    bezeichnung = models.CharField(max_length=50)
    personal = models.ManyToManyField(User, through='Personalzuordnung')

    def __str__(self):
        return f"Nr.: {self.numerischername} bezeichung: {self.bezeichnung}"

class Personalzuordnung(models.Model):

    """
    Das Modell für die Personalzuordnung
    Die Organisationseinheit wird über die Tabelle Personalzuordnung mit dem User verknüpft
    """

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


# Personaltemplates

class Addresatentemplate(models.Model):
    """
    model for the address template
    This model defines the address template used for various purposes, such as assessments or notifications.

    Das Modell für die Adresstemplates
    Dieses Modell definiert das Adresstemplate, das für verschiedene Zwecke wie Beurteilungen oder Benachrichtigungen verwendet wird.
    """

    adressatentemplatebezeichnung = models.CharField(max_length=255) 


    def __str__(self):
        return f'Abt. {self.adressatentemplatebezeichnung}'
    
class User_Addresatentemplate_zuordnung(models.Model):
    """
    Model for the user to address template mapping
    This model maps users to address templates, allowing for specific templates to be assigned to users.
    Many-to-many relationships can be established through this model, allowing for flexible associations between users and address templates.

    Das Modell für die User Addresatentemplate Zuordnung
    Dieses Modell ordnet Benutzer zu Adresstemplates zu, sodass spezifische Templates Benutzern zugewiesen werden können.
    Many-to-Many-Beziehungen können über dieses Modell hergestellt werden, was flexible Zuordnungen zwischen Benutzern und Adresstemplates ermöglicht.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    User_Addresatentemplate_zuordnung = models.ForeignKey(Addresatentemplate, on_delete=models.CASCADE) 

    def __str__(self):
        return f'User {self.user} | Adresstemplate: {self.User_Addresatentemplate_zuordnung}'


# Beurteilungstemplates

class Beurteilungstemplate(models.Model):

    """
    Model for the assessment template
    sets the name for a assesment template. All details are contained in the models connected through the foreign key
    
    Das Modell für die Beurteilungstemplates
    Das Beurteiliungstemplate ist die Klammer für alle weiteren Details der Beurteilungsart
    """

    beurteilungstemplate_bezeichnung = models.CharField(max_length=255 )
    

    def __str__(self):
        return f'TEMPLATE {self.beurteilungstemplate_bezeichnung}'

class Beurteilungsgliederung(models.Model):
    """
    Model for the assessment structure
    The assessment criteria are summarized within the assessment structure and can be grouped accordingly

    Das Modell für die Beurteilungsgliederung
    Die Beurteilungskriterien werden innerhalb der Beurteilungsgliederung zusammengefasst und können so gruppiert werden"""

    gliederung = models.CharField(max_length=50)
    order = models.IntegerField()
    beurteilungstemplate = models.ForeignKey(Beurteilungstemplate, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Beurteilungsgliederung {self.gliederung} | Template: {self.beurteilungstemplate}'

class Beurteilungsauspraegungen(models.Model):
    """
    Model for the assessment characteristics
    The assessment characteristics are the values by which the criteria that are alligned can be assessed within the assessment template
    
    Das Modell für die Beurteilungsausprägungen
    Die Beurteilungsausprägungen sind die Werte, mit denen die Kriterien, die alle auf das Beurteilungstemplate abgestimmt sind, bewertet werden können"""

    beurteilungsausprägung = models.CharField(max_length=50)
    punktwertmax = models.IntegerField()
    punktwertmin = models.IntegerField()

    def __str__(self):
        return f'Ausprägung {self.beurteilungsausprägung}'
        
class Beurteilungsmerkmale(models.Model):
    """
    Model for the assessment criteria
    The assessment criteria are the criteria by which assesment for the assessed person will happen within the assessment template

    Das Modell für die Beurteilungsmerkmale
    Die Beurteilungsmerkmale sind die Kriterien, mit denen die Beurteilung für die beurteilte Person innerhalb des Beurteilungstemplates erfolgt
    """
    
    beurteilungsmerkmal = models.CharField( max_length=50)
    untergruppe = models.ForeignKey(Beurteilungsgliederung, on_delete=models.CASCADE)
    beurteilungstemplate = models.ForeignKey(Beurteilungstemplate, on_delete=models.CASCADE)
    beurteilungsauspraegungen = models.ForeignKey(Beurteilungsauspraegungen, on_delete=models.CASCADE)

    def __str__(self):
        return f'Beurteilungsmerkmal {self.beurteilungsmerkmal}'

# Beurteilungen 

class Beurteilungsadressaten(models.Model):
    beurteilungstemplate = models.ForeignKey(Beurteilungstemplate, on_delete=models.CASCADE)
    addresatentemplate = models.ForeignKey(Addresatentemplate, on_delete=models.CASCADE, )
    def __str__(self):
        return f'Ausprägung {self.beurteilungstemplate} Addresat {self.addresatentemplate}'
    
class Beurteilungstemplate_Beurteiler(models.Model):
    """
    Das Modell für die Beurteilungstemplate Beurteiler
    Die Beurteiler werden dem Beurteilungstemplate zugeordnet
    """

    beurteilungstemplate = models.ForeignKey(Beurteilungstemplate, on_delete=models.CASCADE)
    beurteiler = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Beurteiler {self.beurteilungstemplate} | Addresat {self.beurteiler}'

#Beurteilung

class Beurteilungen(models.Model):
    beurteilung_bez = models.CharField(max_length=255)
    beurteilung_erl = models.CharField(max_length=255)
    beurteilungstemplate = models.ForeignKey(Beurteilungstemplate, on_delete=models.CASCADE)
    beurteilung_frist = models.DateField()
    beurteilung_erläuterung = models.TextField()
    beurteilter = models.ForeignKey(User, on_delete=models.CASCADE)
    beurteilung_abgeschlossen = models.BooleanField(default=False)
 
    
    def __str__(self):
        return f'be: {self.beurteilung_bez}| MA. {self.beurteilter}'
    
class Beurteilung_beurteiler(models.Model):
    """
    Das Modell für die Beurteilung Beurteiler
    Die Beurteiler werden der Beurteilung zugeordnet
    """

    beurteilung = models.ForeignKey(Beurteilungen, on_delete=models.CASCADE)
    beurteiler = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Beurteilung {self.beurteilung} | Beurteiler {self.beurteiler}'


class Beurteilung_Beurteilungsmerkmale(models.Model):
    beurteilung = models.ForeignKey(Beurteilungen, on_delete=models.CASCADE)
    be_merkmal = models.ForeignKey(Beurteilungsmerkmale, on_delete=models.CASCADE)
    be_auspraegung = models.ForeignKey(Beurteilungsauspraegungen, on_delete=models.CASCADE, null=True, blank=True)
    be_kommentar = models.TextField()
    beurteiler = models.ForeignKey(User, on_delete=models.CASCADE)
    beurteilung_timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'be: {self.beurteilung}| Merkmal: {self.be_merkmal}'



