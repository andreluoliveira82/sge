from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Outflow


@receiver(post_save, sender=Outflow)
def update_stock(sender, instance, created, **kwargs):
    """
    Update stock when outflow is created or updated.
    """
    # somente se o lançamento estiver sendo criado, e não atualizado.
    if created:
        if instance.quantity > 0:
            instance.product.quantity -= instance.quantity
            instance.product.save()
