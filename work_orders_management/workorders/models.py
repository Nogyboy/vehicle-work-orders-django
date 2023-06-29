from django.db import models
from vehicles.models import Vehicle
# Create your models here.


class WorkOrders(models.Model):
    # Status Choices
    STATUS_CHOICES = (
        ('P', 'Pendiente'),
        ('T', 'Trabajando'),
        ('L', 'Listo para entrega'),
        ('F', 'Finalizado'),
    )

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

    def __str__(self):
        return self.vehicle.plate

    class Meta:
        verbose_name = 'Orden de trabajo'
        verbose_name_plural = 'Ordenes de trabajo'