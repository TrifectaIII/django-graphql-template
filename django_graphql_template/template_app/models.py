from django.db import models

# Define database models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=True, blank=True)

    author = models.ForeignKey(
        'Author',
        on_delete=models.CASCADE,
        related_name='books'
    )

    genre = models.ForeignKey(
        'Genre',
        on_delete=models.CASCADE,
        related_name='books'
    )

    def __str__(self):
        return "{} by {}".format(self.name, self.author.name)
