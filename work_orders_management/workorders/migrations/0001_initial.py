# Generated by Django 4.2.2 on 2023-06-29 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicles', '0003_alter_vehicle_plate'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('P', 'Pendiente'), ('T', 'Trabajando'), ('L', 'Listo para entrega'), ('F', 'Finalizado')], default='P', max_length=1)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle')),
            ],
            options={
                'verbose_name': 'Orden de trabajo',
                'verbose_name_plural': 'Ordenes de trabajo',
            },
        ),
    ]
