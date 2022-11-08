from django.db import models


class Project(models.Model):
    class Meta:
        db_table = "project"

    title = models.CharField(max_length=100)

    description = models.TextField()

    technology = models.CharField(max_length=20)

    image = models.FilePathField(path='/img', recursive=True)
