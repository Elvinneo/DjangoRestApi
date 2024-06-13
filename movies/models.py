from django.db import models


class Movies(models.Model):
    title=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    year=models.CharField(max_length=30)
    score=models.CharField(max_length=30)
    image=models.FileField(null=True,blank=True)
    def __str__(self):
        return self.title