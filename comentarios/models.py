from django.db import models

# Create your models here.

class Comentario(models.Model):
    commentary = models.TextField(null=False, blank=True, help_text="Realiza una publicacion ahora!")
    updatedAt = models.DateField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    #La idea es mostrar quien hizo el comentario

    class Meta:
        verbose_name = ["commentary"]

    def __str__(self):
        return self.commentary
