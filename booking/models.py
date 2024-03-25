from django.db import models
from datetime import time, date, timedelta
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.core.exceptions import ValidationError


# Create your models here.
class Booking(models.Model):
    """
    Stores the data for a single instance of booking a table
    """
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(
        max_length=30,
        blank=False,
        null=True,
        validators=[RegexValidator("[a-zA-Z]")],
    )
    lname = models.CharField(
        max_length=30,
        blank=False, null=True,
        validators=[RegexValidator("[a-zA-Z]")],
    )
    email = models.EmailField(null=True, blank=False)
    TABLE = (
        (1, "Table 1 - 4 Guests"),
        (2, "Table 2 - 2 Guests"),
        (3, "Table 3 - 2 Guests"),
        (4, "Table 4 - 4 Guests"),
        (5, "Table 5 - 4 Guests"),
        (6, "Table 6 - 8 Guests"),
        (7, "Table 7 - 4 Guests"),
        (8, "Table 8 - 4 Guests"),
        (9, "Table 9 - 4 Guests"),
        (10, "Table 10 - 4 Guests"),
        (11, "Table 11 - 4 Guests"),
        (12, "Table 12 - 6 Guests"),
        (13, "Table 13 - 4 Guests"),
        (14, "Table 14 - 6 Guests"),
    )
    table = models.IntegerField(null=False, blank=False, choices=TABLE)
    # table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False, validators=[MinValueValidator(limit_value=date.today())])
    TIME_SLOTS = (
            (time(11, 0), "11:00 AM"),
            (time(11, 30), "11:30 AM"),
            (time(12, 0), "12:00 PM"),
            (time(12, 30), "12:30 PM"),
            (time(13, 0), "1:00 PM"),
            (time(13, 30), "1:30 PM"),
            (time(14, 0), "2:00 PM"),
            (time(14, 30), "2:30 PM"),
            (time(15, 0), "3:00 PM"),
            (time(15, 30), "3:30 PM"),
            (time(16, 0), "4:00 PM"),
            (time(16, 30), "4:30 PM"),
            (time(17, 0), "5:00 PM"),
            (time(17, 30), "5:30 PM"),
            (time(18, 0), "6:00 PM"),
            (time(18, 30), "6:30 PM"),
            (time(19, 0), "7:00 PM"),
            (time(19, 30), "7:30 PM"),
            (time(20, 0), "8:00 PM"),
            (time(20, 30), "8:30 PM"),
            (time(21, 0), "9:00 PM"),
            (time(21, 30), "9:30 PM"),
            (time(22, 0), "10:00 PM"),
        )
    time = models.TimeField(null=True, blank=False, choices=TIME_SLOTS)
    # time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    end_time = models.TimeField(null=True, blank=True)  # End time calculated dynamically
    num_guest = models.IntegerField(
        blank = False,
        null = False,
        default = 1,
        validators=[MinValueValidator(1), MaxValueValidator(8)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

def clean(self):
    # Ensure the table has sufficient capacity for the booking
    table_capacity = {
        '1': 4,  # Capacity for Table 1
        '2': 2,  # Capacity for Table 2
        '3': 2,  # Capacity for Table 3
        '4': 4,  # Capacity for Table 4
        '5': 4,  # Capacity for Table 5
        '6': 8,  # Capacity for Table 6
        '7': 4,  # Capacity for Table 7
        '8': 4,  # Capacity for Table 8
        '9': 4,  # Capacity for Table 9
        '10': 4,  # Capacity for Table 10
        '11': 4,  # Capacity for Table 11
        '12': 6,  # Capacity for Table 12
        '13': 4,  # Capacity for Table 12
        '14': 6,  # Capacity for Table 14
    }

    
    if self.num_guest > table_capacity.get(str(self.table), 0):
        raise ValidationError("The table's capacity is insufficient for this booking.")

    # Calculate end time based on start time (time_slot) and duration (1.5 hours)
    if self.time:
        duration = timedelta(hours=1, minutes=30)
        self.end_time = (self.time + duration).time()

    # Ensure the selected time slot and date are valid
    existing_bookings = Booking.objects.filter(date=self.date, time=self.time)
    total_guest = sum(booking.num_guest for booking in existing_bookings)
    if total_guest + self.num_guest > table_capacity.get(str(self.table), 0):
        raise ValidationError("The selected time slot is unavailable.")

def save(self, *args, **kwargs):
    try:
        self.full_clean() # Perform full validation before saving
    except ValidationError as e:
        # Handle the validation error
        # You can raise the error or display an error message
        raise e
    super().save(*args, **kwargs)

