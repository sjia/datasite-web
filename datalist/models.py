from django.db import models

# Create your models here.
class Datalist(models.Model):
    # fields = ("id", "name", "city", "Cardnumber", "Phonenumber", "Created", "Token")
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    city = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=50,default="User0")
    city = models.CharField(max_length=50, default="LA")
    cardnumber=models.TextField(max_length=500, default="5105105105105100")
    phonenumber=models.TextField(max_length=50, default="(319)-883-4480")
    created=models.TextField(max_length=500, default="Sun, 23 Feb 2020 08:18:51 GMT")
    token=models.TextField(max_length=500, default="7f38e7a645fbd1b3c68fbc75ecd62d24")
    class meta:
        managed=False
        db_table='datalist_datalist'
    def __str__(self):
        return self.name