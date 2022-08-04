from distutils.command.upload import upload
from os import link
from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class MasDatosUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    descripcion = RichTextField(null=True)
    link = RichTextField(null=True)
