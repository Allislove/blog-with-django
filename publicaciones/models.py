from django.db import models
from comentarios.models import Comentario
from tags.models import Tag
from usuarios.models import User

#Una publicacion puede tener muchos tags y muchos comentarios
# Create your models here.
class Publicacion(models.Model):
    content = models.TextField(blank=True)
    likes = models.IntegerField(default=0)
    #Aqui debo de extraer el creador del post para identificarlo
    createdAt = models.DateTimeField(auto_now_add=True)

    #Relations
    comentario = models.ManyToManyField(Comentario, related_name="Publicacion", blank=True)
    tags = models.ManyToManyField(Tag, related_name="Publicacion", blank=True)
    #Un usuario puede hacer muchos post, y no se puede publicar sin ser un usuario, entonces algunos campos los dejo por defecto
    user = models.ForeignKey(User, related_name="Publicacion", on_delete=models.CASCADE)

    class Meta:
        ordering = ['content']



    def __str__(self):
        return self.content