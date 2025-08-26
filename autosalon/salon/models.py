from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.name


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="cars")
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['-year']
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return f"{self.brand.name} - {self.name}"

