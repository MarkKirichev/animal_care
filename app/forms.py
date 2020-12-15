from django import forms
from app.models import Animal


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        exclude = ('is_cured',)


