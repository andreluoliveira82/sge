from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
    ListView,
)
from .models import Product
from .forms import ProductForm
from categories.models import Category
from brands.models import Brands


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "products"
    paginate_by = 10

    def get_queryset(self):
        """
        Filtra o queryset com base no parâmetro 'name' na query string.
        """
        queryset = super().get_queryset().order_by("id")

        # Filtra o queryset com base no parâmetro 'title' na query string.
        title = self.request.GET.get("title")
        if title:
            queryset = queryset.filter(title__icontains=title)

        # Filtra o queryset com base no parâmetro 'serie_number' na query string.
        serie_number = self.request.GET.get("serie_number")
        if serie_number:
            queryset = queryset.filter(serie_number__icontains=serie_number)

        # Filtra o queryset com base no parâmetro 'category' na query string.
        category = self.request.GET.get("category")
        if category:
            queryset = queryset.filter(category__id=category)

        # Filtra o queryset com base no parâmetro 'brand' na query string.
        brand = self.request.GET.get("brand")
        if brand:
            queryset = queryset.filter(brand__id=brand)

        return queryset

    def get_context_data(self, **kwargs):
        """
        Adiciona as categorias e marcas ao contexto da view.
        """
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["brands"] = Brands.objects.all()
        return context


class ProductCreateView(CreateView):
    model = Product
    template_name = "product_create.html"
    context_object_name = "products"
    form_class = ProductForm
    success_url = reverse_lazy("product_list")


class ProductDetailsView(DetailView):
    model = Product
    template_name = "product_details.html"
    context_object_name = "product"


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "product_update.html"
    context_object_name = "product"
    form_class = ProductForm
    success_url = reverse_lazy("product_list")


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "product_delete.html"
    context_object_name = "product"
    success_url = reverse_lazy("product_list")
