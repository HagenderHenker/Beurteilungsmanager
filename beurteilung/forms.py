from django.forms import ModelForm
from django import forms
from .models import Beurteilung, BeurteilungTemplate, BeurteilungGliederung, BeurteilungAuspraegung


class BeurteilungForm(ModelForm):
    class Meta:
        model = Beurteilung
        fields = ['beurteilung_bez', 'beurteilung_erl', 'beurteilung_frist', 'beurteilung_erläuterung', 'beurteilter']
        widgets = {
            'beurteilung_frist': forms.DateInput(attrs={'type': 'date'}),
            'beurteilung_erläuterung': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
