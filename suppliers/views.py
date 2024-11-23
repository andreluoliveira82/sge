from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
    ListView,
)
from .models import Supplier
from .forms import SupplierForm


class SupplierListView(ListView):
    model = Supplier
    template_name = "supplier_list.html"
    context_object_name = "suppliers"
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


class SupplierCreateView(CreateView):
    model = Supplier
    template_name = "supplier_create.html"
    context_object_name = "suppliers"
    form_class = SupplierForm
    success_url = reverse_lazy("supplier_list")


class SupplierDetailsView(DetailView):
    model = Supplier
    template_name = "supplier_details.html"
    context_object_name = "supplier"


class SupplierUpdateView(UpdateView):
    model = Supplier
    template_name = "supplier_update.html"
    context_object_name = "supplier"
    form_class = SupplierForm
    success_url = reverse_lazy("supplier_list")


class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = "supplier_delete.html"
    context_object_name = "supplier"
    success_url = reverse_lazy("supplier_list")
