from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.IntegerField()

    def __str__(self):
        return self.name  
        
        
class Booking(models.Model):
    user_name = models.CharField(max_length=100)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    travelers = models.IntegerField()

    def __str__(self):
        return f"{self.user_name} - {self.destination.name}"        