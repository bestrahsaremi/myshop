from django.db import models
from datetime import datetime

class Product(models.Model):
    name = models.CharField(max_length=120, blank=False)
    description = models.CharField(max_length=400, blank=False)
    image = models.ImageField(upload_to="products", blank=False)
    created_at=models.DateTimeField(default=datetime.now(), blank=False)

    def __str__(self):
        return self.name