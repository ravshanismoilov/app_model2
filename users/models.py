from django.db import models



class User(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    country = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return f"{self.name} {self.country}"

