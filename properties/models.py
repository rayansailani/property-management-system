from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.


class PropertyForRent(models.Model):
    owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    property_name = models.CharField(max_length=30)
    address = models.TextField()
    floor_no = models.CharField(blank=True, default="Ground", max_length=10)
    no_rooms = models.IntegerField()
    rent = models.IntegerField()
    security_deposit = models.IntegerField(default=0)
    is_occupied = models.BooleanField(default=False)
    image1 = models.ImageField(
        default='house_images/house.jpg', upload_to='house_images/')
    image2 = models.ImageField(
        default='house_images/house.jpg', upload_to='house_images/')
    image3 = models.ImageField(
        default='house_images/house.jpg', upload_to='house_images/')
    image4 = models.ImageField(
        default='house_images/house.jpg', upload_to='house_images/')

    description = models.TextField(max_length=1000, default=" ")
    has_maintainer = models.BooleanField(default=False)

    def __str__(self):
        return self.property_name + ' - ' + self.floor_no

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties for Rent"


class PropertyForSale(models.Model):
    khata = (
        ("A", "A-Khata"),
        ("B", "B-Khata"),
    )
    owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    # no = models.IntegerField()
    # locality = models.CharField(max_length=50)
    # area = models.CharField(max_length=50)
    # city = models.CharField(max_length=50)
    # state = models.CharField(max_length=50)
    address = models.TextField(max_length=1000)
    width = models.IntegerField()
    length = models.IntegerField()
    cost_sqft = models.IntegerField()
    ceritification = models.CharField(
        choices=khata, default="B-Khata", max_length=8)
    description = models.TextField(max_length=1000, default=" ")

    def __str__(self):
        return self.owner.username + " - " + str(self.address)

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties for Sale"


class Appointment(models.Model):
    owner = models.ForeignKey(
        User, related_name="ppty_owner", default=None, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    property = models.ForeignKey(
        PropertyForSale, default=None, on_delete=models.CASCADE)
    date_appointement = models.DateField()
    time_appointment = models.TimeField()

    def __str__(self):
        return str(self.date_appointement) + " - " + str(self.time_appointment)

    class Meta:
        verbose_name = "Appointment "
        verbose_name_plural = "Appointments for sale property"


class visit(models.Model):
    owner = models.ForeignKey(
        User, related_name="ppty_owner_rent", default=None, on_delete=models.CASCADE
    )
    visitor = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE
    )
    property = models.ForeignKey(
        PropertyForRent, default=None, on_delete=models.CASCADE
    )
    date_appointement = models.DateField()
    time_appointment = models.TimeField()

    def __str__(self):
        return str(self.date_appointement) + " - " + str(self.time_appointment)

    class Meta:
        verbose_name = "Appointment "
        verbose_name_plural = "Appointments for rental property"
