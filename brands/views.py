from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
    ListView,
)
from .models import Brands
from .forms import BrandForm


class BrandListView(ListView):
    model = Brands
    template_name = "brand_list.html"
    context_object_name = "brands"
    paginate_by = 10

    def get_queryset(self):
        """
        Filtra o queryset com base no parâmetro 'name' na query string.
        """
        queryset = super().get_queryset().order_by("id")
        name = self.request.GET.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class BrandCreateView(CreateView):
    model = Brands
    template_name = "brand_create.html"
    context_object_name = "brands"
    form_class = BrandForm
    success_url = reverse_lazy("brand_list")


class BrandDetailsView(DetailView):
    model = Brands
    template_name = "brand_details.html"
    context_object_name = "brand"


class BrandUpdateView(UpdateView):
    model = Brands
    template_name = "brand_update.html"
    context_object_name = "brand"
    form_class = BrandForm
    success_url = reverse_lazy("brand_list")


class BrandDeleteView(DeleteView):
    model = Brands
    template_name = "brand_delete.html"
    context_object_name = "brand"
    success_url = reverse_lazy("brand_list")
