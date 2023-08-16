from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Laboratory(models.Model):
    name = models.CharField(max_length=70)
    code = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Laboratory"
        verbose_name_plural = "Laboratorys"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Laboratory_detail", kwargs={"pk": self.pk})
    
class StudentType(models.Model):
    name = models.CharField(max_length=70)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "StudentType"
        verbose_name_plural = "StudentTypes"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("StudentType_detail", kwargs={"pk": self.pk})


class Sponsor(models.Model):
    name = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=70)
    address = models.TextField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Sponsor"
        verbose_name_plural = "Sponsors"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Sponsor_detail", kwargs={"pk": self.pk})

