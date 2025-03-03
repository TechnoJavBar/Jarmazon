# Generated by Django 5.1.3 on 2025-02-20 18:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionAlm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidoweb',
            name='usuario',
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('pvpTotal', models.IntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionAlm.producto', verbose_name='producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
            ],
            options={
                'verbose_name': 'pedido',
                'verbose_name_plural': 'pedidos',
                'unique_together': {('producto', 'usuario', 'fecha')},
            },
        ),
        migrations.DeleteModel(
            name='DetallePedido',
        ),
        migrations.DeleteModel(
            name='PedidoWeb',
        ),
    ]
