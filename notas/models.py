from django.db import models

class Nota(models.Model):
    nombre = models.CharField(max_length=140)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True) 
    ultima_modificacion = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.nombre