from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Seats capacity
SEATS = (
    (2, '2'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
)

class Table(models.Model):
    """
    Table Models, contais table number and the seats capacity
    """
    table_number = models.CharField(max_length=10)
    seats = models.IntegerField(default=2, choices=SEATS)
    # slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(default=timezone.now) 

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Table number {self.table_number}"

    def increment_reservations(self):
        self.num_of_reservations += 1
        self.save()

    def decrement_reservations(self):
        if self.num_of_reservations > 0:
            self.num_of_reservations -= 1
            self.save()

class Reservation(models.Model):
    """
    Booking's Model
    """
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True) #when was it booked
    guest_name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="guest_name"
    )
    guest_count = models.IntegerField(default=2, choices=SEATS)
    canceled = models.BooleanField(default=False)

    # Might need a time slot selection

    def __str__(self):
        return f"Reservertion number {self.id}"
