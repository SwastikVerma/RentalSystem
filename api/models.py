from django.db import models
from django.contrib.auth.models import AbstractUser



#     def __str__(self):
#         return self.username +','+ self.email
class Customer(AbstractUser):
    email = models.EmailField(unique=True)
    # user_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.username
    
class CarModel(models.Model):
    Category = models.CharField(max_length=50,choices=
                          (('SUV','SUV'),
                           ('Prime','Prime'),
                           ('Sedan','Sedan'),
                           ('Electic Car','Electric Car')
                           ))
    model = models.CharField(max_length=50)
    number_plate = models.CharField(max_length=10)
    current_city = models.CharField(max_length=50)
    rent_per_hour = models.IntegerField()
    car_id = models.AutoField(primary_key=True)
    # rent_history = models.

    def __str__(self):
        return self.number_plate +" - "+ self.model
    


class Rent_history(models.Model):
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    amount = models.IntegerField()

    car=models.ForeignKey(CarModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.amount +" - "+ self.origin

