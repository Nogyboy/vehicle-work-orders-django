from django.db import models
from django.contrib.auth.models import User
import requests
from django.conf import settings
import os
from django.core.files import File
from io import BytesIO
from django.db.models.signals import pre_delete
from django.dispatch import receiver


def get_unsplash_image(request):
    access_key = settings.UNSPLASH_API_KEY

    # Request a random image from Unsplash API
    url = f'https://api.unsplash.com/photos/random/?client_id={access_key}&query=car&orientation=landscape&count=1'
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        first_result = data[0]  # Get the first result
        image_url = first_result['urls']['regular']
        image_name = first_result['alt_description']

        return image_url, image_name
    else:
        return None, None

class Vehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plate = models.CharField(max_length=10, unique=True)
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
    
    # Validate if the user select an image
    def save(self, *args, **kwargs):
        if not self.image:
            image_url, image_name = get_unsplash_image(self)
            if image_url and image_name:
                # Descargar la imagen desde la URL
                response = requests.get(image_url)
                if response.status_code == 200:
                    # Obtener los datos de la imagen
                    image_data = response.content

                    # Crear un nombre de archivo único utilizando el campo "plate" y la extensión de archivo
                    file_name = f"{self.plate}.jpg"

                    # Crear un objeto File a partir de los datos de la imagen
                    file_object = File(BytesIO(image_data), name=file_name)

                    # Asignar el objeto File al campo "image" del modelo
                    self.image.save(file_name, file_object)

        super().save(*args, **kwargs)


@receiver(pre_delete, sender=Vehicle)
def delete_image(sender, instance, **kwargs):
    # Delete the image from the storage
    if instance.image:
        file_path = instance.image.path
        if os.path.exists(file_path):
            os.remove(file_path)




