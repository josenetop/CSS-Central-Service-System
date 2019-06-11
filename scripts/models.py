from django.db import models
from datetime import timezone

# Create your models here.
class Scripts(models.Model):
    dataCadastro = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    titulo = models.CharField(max_length=250, null=True, blank=True)
    texto = models.TextField()

    def __str__(self):
        return self.titulo