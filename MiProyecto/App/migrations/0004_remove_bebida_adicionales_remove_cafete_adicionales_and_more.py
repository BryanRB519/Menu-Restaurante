# Generated by Django 5.1.1 on 2024-10-10 01:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_adicional_bebida_adicionales_cafete_adicionales_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bebida',
            name='adicionales',
        ),
        migrations.RemoveField(
            model_name='cafete',
            name='adicionales',
        ),
        migrations.RemoveField(
            model_name='comida',
            name='adicionales',
        ),
        migrations.RemoveField(
            model_name='guarnicion',
            name='adicionales',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='adicionales',
        ),
        migrations.RemoveField(
            model_name='postre',
            name='adicionales',
        ),
        migrations.AddField(
            model_name='bebida',
            name='adicional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.adicional'),
        ),
        migrations.AddField(
            model_name='cafete',
            name='adicional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.adicional'),
        ),
        migrations.AddField(
            model_name='comida',
            name='adicional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.adicional'),
        ),
        migrations.AddField(
            model_name='guarnicion',
            name='adicional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.adicional'),
        ),
        migrations.AddField(
            model_name='postre',
            name='adicional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.adicional'),
        ),
    ]
