from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    average_cost = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    photo = models.ImageField(upload_to='product_photos')

    def __str__(self):
        return self.name

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author_photo = models.ImageField(upload_to='review_author_photos', null=True, blank=True)

    def __str__(self):
        return f'Review by {self.author.username} on {self.product.name}'
    
class SecurityQuestion(models.Model):
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.question