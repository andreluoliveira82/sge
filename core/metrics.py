from django.utils.formats import number_format
from products.models import Product


def get_product_metrics():
    """
    Retorna um dicionário com as métricas de produtos.
    """
    products = Product.objects.all()

    total_quantity = sum(product.quantity for product in products)
    total_cost_price = sum(product.cost_price for product in products)
    total_selling_price = sum(product.salling_price for product in products)
    total_profit = total_selling_price - total_cost_price

    product_metrics = {
        "total_quantity": total_quantity,
        "total_cost_price": number_format(
            total_cost_price, decimal_pos=2, force_grouping=True
        ),
        "total_selling_price": number_format(
            total_selling_price, decimal_pos=2, force_grouping=True
        ),
        "total_profit": number_format(total_profit, decimal_pos=2, force_grouping=True),
    }

    return product_metrics
