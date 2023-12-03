from django.db import models

# Create your models here.

class Responses(models.Model):
    responses = models.TextField("response")
    date = models.DateTimeField("date")
