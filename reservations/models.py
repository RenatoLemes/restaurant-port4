from django.db import models


class Table(models.Model):
    table_number = models.CharField(max_length=10)
    capacity = models.PositiveIntegerField()

class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    guest_name = models.CharField(max_length=100)
    guest_count = models.PositiveIntegerField()
    canceled = models.BooleanField(default=False)
