from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

CLUB = (
    (0,"Writing"),
    (1,"Debating"),
    (2,"Quizzing"),
    (3,"Secy")
)

STATUS = (
    (0,"Current"),
    (1,"Former")
)

class Team(models.Model):
    name=models.CharField(max_length=100)
    fb = models.CharField()
    mail = models.CharField()
    image = models.ImageField(upload_to = 'team_img', blank=True, default='event_img/default.jpg')

    class Meta:
        ordering = ['-date']
    def __str__(self):
        return self.title