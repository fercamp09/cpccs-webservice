from django.db import models

# Create your models here.
class Sector(models.Model): 
    nombre = models.CharField(max_length=255) 
    descripcion = models.CharField(max_length=255) 
    control = models.CharField(max_length=5) 
    mensaje = models.CharField(max_length=255)
	
    class Meta:
        db_table = 'sector'
        ordering = ('nombre',) 
 
    def __str__(self): 
        return self.nombre 

class Usuario(models.Model): 
    nome = models.CharField(max_length=20) 
    email = models.CharField(max_length=30) 
    telefone = models.CharField(max_length=12) 
    
    class Meta:
        db_table = 'usuario'
        ordering = ('nome',) 
 
    def __str__(self): 
        return self.nome 
