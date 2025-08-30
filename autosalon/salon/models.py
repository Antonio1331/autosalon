from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Brend nomi")
    country = models.CharField(max_length=100, verbose_name="Mamlakat")

    class Meta:
        ordering = ['name']
        verbose_name = "Brend"
        verbose_name_plural = "Brendlar"

    def __str__(self):
        return self.name


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="cars", verbose_name="Brendi")
    name = models.CharField(max_length=100, verbose_name="Mashina nomi")
    year = models.IntegerField(verbose_name="Yili")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    image = models.ImageField(upload_to="cars/", blank=True, null=True, verbose_name="Rasmi")
    is_available = models.BooleanField(default=True, verbose_name="Sotuvda bormi?")

    class Meta:
        ordering = ['-year']
        verbose_name = "Mashina"
        verbose_name_plural = "Mashinalar"

    def __str__(self):
        return f"{self.brand.name} - {self.name}"


class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="comments", verbose_name="Mashina")
    author = models.CharField(max_length=100, verbose_name="Muallif")
    text = models.TextField(verbose_name="Izoh matni")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo‘shilgan vaqt")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Izoh"
        verbose_name_plural = "Izohlar"

    def __str__(self):
        return f"{self.author} → {self.car.name}"

