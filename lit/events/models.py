from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Events(models.Model):
    title=models.CharField(blank=True, max_length=100)
    content = models.TextField(blank=True)
    date = models.DateTimeField(blank=True, default=timezone.now)
    # author = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-date']
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'pk':self.pk})
