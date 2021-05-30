from django.db import models
from django.contrib.auth import get_user_model


class Address(models.Model):
    body = models.CharField(max_length=300)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.body
