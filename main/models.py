from django.db import models
from datetime import date

# Create your models here.

class Language(models.Model):
    kod = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Navbar(models.Model):
    title = models.CharField(max_length=200)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    child_navbars = models.ForeignKey("Navbar", on_delete=models.CASCADE, blank=True, null=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Information(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True)
    full_desc = models.TextField(blank=True)
    mini_desc = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='upload', blank=True)
    job = models.CharField(max_length=200, blank=True)
    pdf = models.FileField(upload_to='upload', blank=True)
    qr = models.CharField(max_length=400,  blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Contact(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=200)
    phone1 = models.CharField(max_length=200)
    phone2 = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    status = models.IntegerField(default=0)
    instagram = models.CharField(max_length=200, blank=True)
    telegram = models.CharField(max_length=200, blank=True)
    youtube = models.CharField(max_length=200, blank=True)
    whatsapp = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.address


class News(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True)
    full_desc = models.TextField(blank=True)
    mini_desc = models.CharField(max_length=200, blank=True)
    video = models.FileField(upload_to="media", null=True, blank=True)
    image = models.ImageField(upload_to='upload', blank=True)
    posted_date = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class Donate(models.Model):
    number_card = models.CharField(max_length=200)
    name_card = models.CharField(max_length=200)
    cvv = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    accept = models.BooleanField(default=False)

    def __str__(self):
        return str(self.price)


class JoinToGroup(models.Model):
    name = models.CharField(max_length=200)
    iin = models.CharField(max_length=200)
    date_birth = models.DateField(default=date.today, blank=True)
    phone_number = models.CharField(max_length=200)
    status = models.IntegerField(default=0)


    def __str__(self):
        return self.name



class Region(models.Model):
    kod = models.CharField(max_length=200, blank=True)
    desc = models.TextField(blank=True)
    longitude = models.CharField(max_length=200, blank=True)
    latitude = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.kod

