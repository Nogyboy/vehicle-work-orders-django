from django.contrib import admin
from django import forms
from .models import WorkOrders
# Register your models here.

class WorkOrderAdminForm(forms.ModelForm):
    class Meta:
        model = WorkOrders
        fields = '__all__'
    
    # Validate if the vehicle selected has not an active work order mean the status is not 'F'
    def clean(self):
        cleaned_data = super().clean()
        vehicle = cleaned_data.get('vehicle')
        if vehicle:
            active_orders = WorkOrders.objects.filter(vehicle=vehicle).exclude(status='F')
            if active_orders.exists():
                if self.instance.pk:
                    if active_orders.first().pk != self.instance.pk:
                        raise forms.ValidationError('El vehículo ya tiene una orden de trabajo activa')
                else:
                    raise forms.ValidationError('El vehículo ya tiene una orden de trabajo activa')
        return cleaned_data
    
@admin.register(WorkOrders)
class WorkOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehicle', 'start_date', 'end_date', 'description', 'status')
    search_fields = ('vehicle__plate', 'start_date', 'end_date', 'description', 'status')
    list_filter = ('start_date', 'end_date', 'status')
    form = WorkOrderAdminForm