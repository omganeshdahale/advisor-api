from django.db import models


class Advisor(models.Model):
    name = models.CharField(max_length=200)
    photo_url = models.URLField()

    def __str__(self):
        return self.name
