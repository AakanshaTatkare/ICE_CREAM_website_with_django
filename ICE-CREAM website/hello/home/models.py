from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    reason=models.TextField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.name 