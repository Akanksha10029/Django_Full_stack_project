from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=2000)
    photo = models.ImageField(upload_to='photos/', blank=True,null=True)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user.username} - Rating: {self.rating} - {self.text[:100]}...'

        

    
    