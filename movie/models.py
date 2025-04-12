from django.db import models

class  Movie(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="img")
    date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name

class Actor(models.Model):
    pass