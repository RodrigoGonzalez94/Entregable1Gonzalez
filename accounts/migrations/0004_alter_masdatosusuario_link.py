# Generated by Django 4.0.5 on 2022-08-04 00:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_masdatosusuario_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masdatosusuario',
            name='link',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
