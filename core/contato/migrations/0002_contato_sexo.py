# Generated by Django 2.2.8 on 2020-06-22 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='sexo',
            field=models.CharField(blank=True, choices=[('F', 'Feminino'), ('M', 'Masculino')], max_length=1),
        ),
    ]
