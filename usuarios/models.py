from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    nickName = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nickName