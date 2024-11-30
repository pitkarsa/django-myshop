from django.db import models

# Create your models here.
class Category(models.Model): # application name_model
    # 
    name= models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE, db_column="catId")

    def __str__(self):
        return self.name