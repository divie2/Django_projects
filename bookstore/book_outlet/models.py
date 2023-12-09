from tabnanny import verbose
from tkinter import CASCADE
from turtle import title
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify


# Create your models here.




class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2, null=True)
    
    def __str__(self):
        return f"{self.name} {self.code}" 
    class Meta():
        verbose_name_plural = "Countries"
    
    
class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=100)
    city = models.CharField(max_length= 100) 
    
    def __str__(self):
        return f"{self.street} {self.city}" 
    class Meta():
        verbose_name_plural = "Address Entries"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100) 
    address = models.OneToOneField(Address, on_delete=models.CASCADE,null=True)
     
    def __str__(self):
      return f"{self.first_name} {self.last_name}"   
    
    # def __str__(self) :
    #     return self.first() 

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=(MinValueValidator(1), MaxValueValidator(5))
    )
    author = models.ForeignKey(Author , on_delete=models.CASCADE,null=True,
                               related_name="books")
    published_books= models.ManyToManyField(Country)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True,null=False,db_index=True)
    
    
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args,**kwargs)
        
     
    def __str__(self):
        return f"{self.title} ({self.rating})"
     