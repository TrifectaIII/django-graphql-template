from django.db import models


class TemplateCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TemplateObject(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=True, blank=True)

    category = models.ForeignKey(
        'TemplateCategory',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
