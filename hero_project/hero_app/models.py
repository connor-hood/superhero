from django.db import models

# Create your models here.


class Hero(models.Model):
    name = models.CharField(max_length=20)
    alter_ego = models.CharField(max_length=30)
    primary_ability = models.CharField(max_length=20)
    secondary_ability = models.CharField(max_length=20)
    catchphrase = models.CharField(max_length=100)

    def __str__(self):
        return self.name
