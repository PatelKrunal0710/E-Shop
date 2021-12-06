from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='Media/product')

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()

    @staticmethod
    def get_products_by_id(id):
        return Product.objects.filter(id__in=id)