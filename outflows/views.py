from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
)
from .models import Outflow
from .forms import OutflowForm


class OutflowListView(ListView):
    model = Outflow
    template_name = "outflow_list.html"
    context_object_name = "outflows"
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


class OutflowCreateView(CreateView):
    model = Outflow
    template_name = "outflow_create.html"
    context_object_name = "outflows"
    form_class = OutflowForm
    success_url = reverse_lazy("outflow_list")


class OutflowDetailsView(DetailView):
    model = Outflow
    template_name = "outflow_details.html"
    context_object_name = "outflow"
