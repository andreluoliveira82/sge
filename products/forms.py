from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "brand",
            "category",
            "title",
            "description",
            "serie_number",
            "cost_price",
            "salling_price",
            "quantity",
        ]
        widgets = {
            "brand": forms.Select(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o nome do produto",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Digite uma breve descrição sobre o produto",
                }
            ),
            "serie_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o numero de serie do produto",
                }
            ),
            "cost_price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o preco de custo do produto",
                }
            ),
            "salling_price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o preco de venda do produto",
                }
            ),
            "quantity": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite a quantidade do produto",
                }
            ),
        }

        labels = {
            "title": "Nome",
            "description": "Descrição",
            "serie_number": "Numero de serie",
            "cost_price": "Preço de custo",
            "salling_price": "Preço de venda",
            "quantity": "Quantidade",
        }
