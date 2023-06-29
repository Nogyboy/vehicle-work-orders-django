from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Vehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plate = models.CharField(max_length=10)
    brand = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='vehicles', null=True, blank=True)

    def __str__(self):
        return self.plate
    
    class Meta:
        verbose_name = 'Vehículo'
        verbose_name_plural = 'Vehículos'
    
    # Validate if the user is a client before saving the vehicle
    # def save(self, *args, **kwargs):
    #     if not(self.user.customuser.is_cliente):
    #         error_message = 'El usuario no es un cliente'
    #         raise ValidationError(error_message, code='invalid')
    #     super(Vehicle, self).save(*args, **kwargs)

