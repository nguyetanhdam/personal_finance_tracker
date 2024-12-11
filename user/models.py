from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.id}_{self.username}" 