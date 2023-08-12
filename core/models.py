from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Laboratory(models.Model):
    name = models.CharField(max_length=70)
    code = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        verbose_name = "laboratory"
        verbose_name_plural = "laboratories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("laboratories-detail", kwargs={"pk": self.pk})
