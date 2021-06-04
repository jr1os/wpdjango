from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    link = models.URLField(verbose_name="Dirección Web", blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True, verbose_name="Data de Creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Data de Actualización")
    

    class Meta:
        verbose_name = "projecto"
        verbose_name_plural = "projectos"
        ordering = ["-create"]
    

    def __str__(self):
        return self.title
    