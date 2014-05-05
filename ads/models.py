# coding: utf-8
# abel
# ruben
# dante

from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)


TIPO_ANUNCIO =(
    ('C', 'Compra'),
    ('V', 'Venta'),
    ('A', 'Alquiler'),
    ('T', 'Trabajo'),
    ('O', 'Otros'),
)


class Elemento(models.Model):
    anuncio = models.CharField(max_length=1, choices=TIPO_ANUNCIO, default='O')
    nombre = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria)
    seccion = models.CharField(max_length=255)
    descripcion = models.TextField()
    publicado_en = models.DateTimeField(auto_now_add=True)
