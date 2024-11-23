from django import forms
from .models import Inflow


class InflowForm(forms.ModelForm):
    class Meta:
        model = Inflow
        fields = [
            "supplier",
            "product",
            "quantity",
            "description",
        ]
        widgets = {
            "supplier": forms.Select(attrs={"class": "form-control"}),
            "product": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Digite uma breve descrição ou observação sobre a entrada",
                }
            ),
        }

        labels = {
            "supplier": "Fornecedor",
            "product": "Produto",
            "quantity": "Quantidade",
            "description": "Descrição",
        }