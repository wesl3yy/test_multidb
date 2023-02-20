from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    birth = models.DateField()
    address = models.CharField(max_length=255)

    class Meta:
        db_table = 'author'
        managed = True


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    hotline = models.CharField(max_length=50)

    class Meta:
        db_table = 'publisher'
        managed = True


class Book(models.Model):
    name = models.CharField(max_length=255)
    publish_date = models.DateField()
    author = models.ForeignKey(Author, verbose_name='author_name', on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, verbose_name='publisher', on_delete=models.CASCADE)

    class Meta:
        db_table = 'book'
        managed = True
