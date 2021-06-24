from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title=models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-date']
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
