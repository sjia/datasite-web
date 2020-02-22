from django.db import models

# Create your models here.
class Datalist(models.Model):
    name = models.CharField(max_length=50)
    # cardnumber = models.BigIntegerField(max_length=10)

    def __str__(self):
        return self.name