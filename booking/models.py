from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.utils import timezone
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Hotel(models.Model):
    name = models.CharField(max_length=50, )
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, default=None)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Hotel, self).save(*args, **kwargs)

def pre_save_hotel_signal(instance, sender,  *args, **kwargs):
    num = 1
    slug = slugify(instance.name)
    exists = Hotel.objects.filter(slug=slug).exists()
    if exists:
        new_slug = slug + "-" + str(num)
        exists = Hotel.objects.filter(slug=new_slug).exists()
        while exists:
            num +=1
            new_slug = slug + "-" + str(num)
            exists = Hotel.objects.filter(slug=new_slug).exists()
        slug = new_slug
    instance.slug = slug

pre_save.connect(pre_save_hotel_signal, sender=Hotel)


class RoomType(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.00'))])
    hotel = models.ForeignKey(Hotel, related_name='room_types', on_delete=models.CASCADE, default="")

    def __str__(self):
        return F"{self.name} room in {self.hotel}"

    class Meta:
        unique_together = ['hotel', 'name']


class Room(models.Model):
    number = models.IntegerField()
    room_type = models.ForeignKey(RoomType, related_name="rooms", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.number)

    class Meta:
        unique_together = ['number', 'room_type']


class Apartment(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.00'))])
    name = models.CharField(max_length=50, )
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE,  null=True)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, null=True)
    check_in = models.DateField(default=timezone.now)
    check_out = models.DateField(default=timezone.now)

















