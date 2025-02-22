from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=123)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Color(models.Model):
    title = models.CharField(max_length=123)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'цвет'
        verbose_name_plural = 'цвета'



class Car(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=123)
    model = models.CharField(max_length=123)
    year = models.SmallIntegerField()
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='media/car_images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'машина'
        verbose_name_plural = 'машины'

class News(models.Model):
    title = models.CharField(max_length=123)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title






