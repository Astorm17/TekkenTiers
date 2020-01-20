from django.db import models

class Character(models.Model):
    character_name = models.CharField(max_length=20)
    character_portrait = models.ImageField(upload_to='portraits/')

    def __str__(self):
        return self.character_name

class Tierlist(models.Model):
    tierlist = models.TextField(null=True)
    




