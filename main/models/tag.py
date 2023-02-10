from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=64)
    id = models.BigAutoField(primary_key=True)
