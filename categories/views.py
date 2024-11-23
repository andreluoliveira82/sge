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
    extra_context = {"title": "Criar Categoria"}
    success_message = "Categoria criada com sucesso!"
    error_message = "Erro ao criar categoria!"
    success_status = 201
    error_status = 400
    success_template = "category_create_success.html"
    error_template = "category_create_error.html"
    success_context = {"message": "Categoria criada com sucesso!"}
    error_context = {"message": "Erro ao criar categoria!"}
    success_redirect = reverse_lazy("category_list")
    error_redirect = reverse_lazy("category_list")
    success_message_code = 201
    error_message_code = 400
    success_message_code_name = "Created"
    error_message_code_name = "Bad Request"
    success_message_code_description = "Created"


class CategoryDetailsView(DetailView):
    model = Category
    template_name = "category_details.html"
    context_object_name = "category"
    extra_context = {"title": "Detalhes da Categoria"}
    success_message = "Categoria detalhada com sucesso!"
    error_message = "Erro ao detalhar categoria!"
    success_status = 200
    error_status = 404
    success_template = "category_details_success.html"
    error_template = "category_details_error.html"
    success_context = {"message": "Categoria detalhada com sucesso!"}
    error_context = {"message": "Erro ao detalhar categoria!"}
    success_redirect = reverse_lazy("category_list")
    error_redirect = reverse_lazy("category_list")
    success_message_code = 200
    error_message_code = 404
    success_message_code_name = "OK"
    error_message_code_name = "Not Found"
    success_message_code_description = "OK"


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = "category_update.html"
    context_object_name = "category"
    form_class = CategoryForm
    success_url = reverse_lazy("category_list")
    extra_context = {"title": "Atualizar Categoria"}
    success_message = "Categoria atualizada com sucesso!"
    error_message = "Erro ao atualizar categoria!"
    success_status = 200
    error_status = 400
    success_template = "category_update_success.html"
    error_template = "category_update_error.html"
    success_context = {"message": "Categoria atualizada com sucesso!"}
    error_context = {"message": "Erro ao atualizar categoria!"}
    success_redirect = reverse_lazy("category_list")
    error_redirect = reverse_lazy("category_list")
    success_message_code = 200
    error_message_code = 400
    success_message_code_name = "OK"


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "category_delete.html"
    context_object_name = "category"
    success_url = reverse_lazy("category_list")
    extra_context = {"title": "Excluir Categoria"}
    success_message = "Categoria excluida com sucesso!"
    error_message = "Erro ao excluir categoria!"
    success_status = 200
    error_status = 400
    success_template = "category_delete_success.html"
    error_template = "category_delete_error.html"
    success_context = {"message": "Categoria excluida com sucesso!"}
    error_context = {"message": "Erro ao excluir categoria!"}
    success_redirect = reverse_lazy("category_list")
    error_redirect = reverse_lazy("category_list")
    success_message_code = 200
    error_message_code = 400
    success_message_code_name = "OK"
