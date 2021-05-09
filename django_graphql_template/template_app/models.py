from django.db import models

# Define database models

class TemplateCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "template categories"

    def __str__(self):
        return self.name

class TemplateObject(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(
        'TemplateCategory',
        on_delete=models.CASCADE,
        related_name='template_objects'
    )

    def __str__(self):
        return self.name
