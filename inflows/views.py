from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
)
from .models import Inflow
from .forms import InflowForm


class InflowListView(ListView):
    model = Inflow
    template_name = "inflow_list.html"
    context_object_name = "inflows"
    paginate_by = 10

    def get_queryset(self):
        """
        Filtra o queryset com base no parâmetro 'name' na query string.
        """
        queryset = super().get_queryset().order_by("id")
        product = self.request.GET.get("product")

        if product:
            queryset = queryset.filter(product__title__icontains=product)
        return queryset


class InflowCreateView(CreateView):
    model = Inflow
    template_name = "inflow_create.html"
    context_object_name = "inflows"
    form_class = InflowForm
    success_url = reverse_lazy("inflow_list")


class InflowDetailsView(DetailView):
    model = Inflow
    template_name = "inflow_details.html"
    context_object_name = "inflow"
