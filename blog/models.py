from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.urls import reverse

class post(models.Model):
    company=models.CharField(max_length=20)
    position=models.CharField(max_length=30)
    package=models.CharField(max_length=20)
    location=models.CharField(max_length=30,blank=True)
    vanue=models.CharField(max_length=20,blank=True,choices=(('IPS','IPS'),('Medicaps','Medicaps'),('Others','others')))
    time=models.DateTimeField(null=True,blank=True)
    last_registration_date=models.DateField(null=True,blank=True)
    description=models.TextField(blank=True)

    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.company



class Comment(models.Model):  # new
    post = models.ForeignKey(
        post,
        on_delete=models.CASCADE,
        related_name='comment',
        blank=True,
    )
    comment = models.TextField(max_length=140)
    posting_date=models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        blank=True,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('post-detail')