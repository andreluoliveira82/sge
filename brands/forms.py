from django import forms
from .models import Brands


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brands
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Digite o nome da marca"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Digite uma breve descrição sobre a marca",
                }
            ),
        }
