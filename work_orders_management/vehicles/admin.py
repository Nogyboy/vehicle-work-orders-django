from django.contrib import admin
from django import forms
from .models import Vehicle
# Register your models here.

class VehicleAdminForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
    
    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get('user')
        if user and not user.customuser.is_cliente:
            raise forms.ValidationError('El usuario no es un cliente')

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'plate', 'brand', 'model', 'year', 'color', 'image')
    search_fields = ('plate', 'brand', 'model', 'year', 'color')
    list_filter = ('user', 'brand', 'model', 'year', 'color')
    form = VehicleAdminForm