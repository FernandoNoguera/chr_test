from django.db import models
from django.contrib.postgres.fields import ArrayField


class Location(models.Model):
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=3)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)


    def __str__(self):
        return self.city


class Extra(models.Model):
    address = models.CharField(max_length=250)
    altitude = models.PositiveIntegerField()
    ebikes = models.PositiveIntegerField()
    has_ebikes = models.BooleanField(default=False)
    last_updated = models.DateTimeField()
    normal_bikes = models.PositiveIntegerField()
    payment = ArrayField(models.CharField(max_length=200), blank=True)
    payment_terminal = models.BooleanField()
    post_code = models.CharField(max_length=50,null=True)
    renting = models.PositiveIntegerField()
    returning = models.PositiveIntegerField()
    slots = models.PositiveIntegerField()
    uid = models.CharField(max_length=250, unique=True)


    def __str__(self):
        return self.uid


class Station(models.Model):
    empty_slots = models.PositiveIntegerField(default=0)
    extra = models.ForeignKey(Extra, on_delete=models.CASCADE)
    free_bikes = models.PositiveIntegerField(default=0)
    id = models.CharField(max_length=250, unique=True, primary_key=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    name =models.CharField(max_length=250)
    timestamp = models.DateTimeField()


    def __str__(self):
        return self.name


class Response(models.Model):
    company = ArrayField(models.CharField(max_length=200), blank=True)
    gbfs_href = models.CharField(max_length=300)
    href = models.CharField(max_length=300)
    id = models.CharField(max_length=250, unique=True, primary_key=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    stations = models.ManyToManyField(Station, related_name='networks')


    def __str__(self):
        return self.name