from django.db import models


class Category(models.Model):
    class Meta:
        db_table = "category"

    name = models.CharField(max_length=20)
