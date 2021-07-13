from django.db import models
from django.utils import timezone
from django.urls import reverse

STATUS = (
    (0,"Writing"),
    (1,"Debating"),
    (2,"Quizzing")
)

class Events(models.Model):
    title=models.CharField(blank=True, max_length=100)
    content = models.TextField(blank=True)
    date = models.DateTimeField(blank=True, default=timezone.now)
    image = models.ImageField(upload_to = 'event_img', blank=True, default='event_img/default.jpg')
    status = models.IntegerField(choices=STATUS)

    class Meta:
        ordering = ['-date']
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'pk':self.pk})
