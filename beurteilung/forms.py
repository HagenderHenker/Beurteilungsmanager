from django.forms import ModelForm
from django import forms
from beurteilung.models import Beurteilungen


class BeurteilungForm(ModelForm):
    class Meta:
        model = Beurteilungen
        fields = ['beurteilung_bez', 'beurteilung_erl', 'beurteilung_frist', 'beurteilung_erläuterung', 'beurteilter']
        widgets = {
            'beurteilung_frist': forms.DateInput(attrs={'type': 'date'}),
            'beurteilung_erläuterung': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
