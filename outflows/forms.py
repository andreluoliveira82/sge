from django import forms
from .models import Outflow


class OutflowForm(forms.ModelForm):
    class Meta:
        model = Outflow
        fields = [
            "supplier",
            "product",
            "quantity",
            "description",
        ]
        widgets = {
            "supplier": forms.Select(
                attrs={"class": "form-control form-control-sm"}
            ),  # Ajustando para menor
            "product": forms.Select(
                attrs={"class": "form-control form-control-sm"}
            ),  # Ajustando para menor
            "quantity": forms.NumberInput(
                attrs={"class": "form-control form-control-sm"}
            ),  # Ajustando para menor
            "description": forms.Textarea(
                attrs={
                    "class": "form-control form-control-sm",  # Ajustando para menor
                    "rows": 3,
                    "placeholder": "Digite uma breve descrição ou observação sobre a saída",
                }
            ),
        }

        labels = {
            "supplier": "Fornecedor",
            "product": "Produto",
            "quantity": "Quantidade",
            "description": "Descrição",
        }
