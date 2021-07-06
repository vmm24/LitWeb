from django.db import models
from django.utils import timezone
from django.urls import reverse

class Mags(models.Model):
    title=models.CharField(blank=True, max_length=100)
    image = models.ImageField(upload_to = 'vivaan_img', blank=True, default='event_img/default.jpg')
    pdf = models.FileField(upload_to='vivaan_pdf', blank=True)

    def __str__(self):
        return self.title