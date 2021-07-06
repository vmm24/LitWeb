from django.db import models
from django.utils import timezone
from django.urls import reverse

class DEvents(models.Model):
    title=models.CharField(blank=True, max_length=100)
    content = models.TextField(blank=True)
    date = models.DateTimeField(blank=True, default=timezone.now)
    # image = models.ImageField(upload_to = 'event_img', blank=True, default='event_img/default.jpg')

    class Meta:
        ordering = ['-date']
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('details', kwargs={'pk':self.pk})
