# Generated by Django 5.1.1 on 2024-10-02 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='cafe_te',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.cafete'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='guarnicion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.guarnicion'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='postre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.postre'),
        ),
    ]
