from django.db import models
from django import forms
from django.contrib.auth.models import User 
from cloudinary.models import CloudinaryField

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    item_image = CloudinaryField('image', default='placeholder')
    allergens = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Comment(models.Model):
  """ 
  Stores a single comment entry related to :model:`auth.User`
  and :model:`menu.Menu`.
  """
  post = models.ForeignKey(
    Menu, on_delete=models.CASCADE, related_name="comments"
  )
  author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="comment_author"
  )
  body = models.TextField()
  approved = models.BooleanField(default=False)
  created_on = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ["created_on"]
  
  def __str__(self):
    return f"Comment {self.body} by {self.author}"