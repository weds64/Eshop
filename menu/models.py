from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse("category", kwargs={"pk": self.pk})
    def __str__(self) -> str:
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits = 999999, decimal_places=2)
    characteristic = models.TextField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

# add products


def menu(request):
    product = Products(name = 'NVIDIA Geforce 1650 Ti')
    product.save()
    product = Products(name = 'Nike React Infinity 3')
    product.save()
    product = Products(name = 'lego city')
    product.save()
    product = Products(name = 'The Greatest Hits Of The 70s Music ')
    product.save()
    product = Products(name = 'Aspirin')
    product.save()
    categories = Products.objects.all()
    return render(request, 'menu/index.html', 
        {
            'categories':categories,
            'title' : "main"
        })