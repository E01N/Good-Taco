from django.db import models


class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.ImageField()
    number_of_people = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()



    def __str__(self):
        return self.name