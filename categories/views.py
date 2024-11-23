from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
    ListView,
)
from .models import Category
from .forms import CategoryForm


class CategoryListView(ListView):
    model = Category
    template_name = "category_list.html"
    context_object_name = "categories"
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


class CategoryCreateView(CreateView):
    model = Category
    template_name = "category_create.html"
    context_object_name = "categories"
    form_class = CategoryForm
    success_url = reverse_lazy("category_list")


class CategoryDetailsView(DetailView):
    model = Category
    template_name = "category_details.html"
    context_object_name = "category"


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = "category_update.html"
    context_object_name = "category"
    form_class = CategoryForm
    success_url = reverse_lazy("category_list")


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "category_delete.html"
    context_object_name = "category"
    success_url = reverse_lazy("category_list")
