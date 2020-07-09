from django.db import models

# Create your models here.
class Brand(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Model(models.Model):
    title = models.CharField(max_length=20)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return '{} ({})'.format(self.title, self.brand.title)


class Car(models.Model):
    TRANS_TYPE = (
        (1, "механика"),
        (2, "автомат"),
        (3, "робот")
    )
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    release_year = models.IntegerField()
    transmission = models.SmallIntegerField(choices=TRANS_TYPE)
    color = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True)

    def __str__(self):
        return '{} ({})'.format(self.model, self.release_year)


