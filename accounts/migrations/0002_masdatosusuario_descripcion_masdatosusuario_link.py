# Generated by Django 4.0.5 on 2022-08-03 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='masdatosusuario',
            name='descripcion',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='masdatosusuario',
            name='link',
            field=models.TextField(null=True),
        ),
    ]
