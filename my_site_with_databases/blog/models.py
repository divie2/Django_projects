from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        
        return f"{self.caption}"
    

class Author(models.Model):
    First_name = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Email_Address = models.EmailField( max_length=254)
    
    def __str__(self) -> str:
        return f"{self.First_name} {self.Lastname} "
    
class Post(models.Model):
    Title =models.CharField(max_length=100)
    Excerpt =models.CharField(max_length=200)
    Image_name =models.CharField(max_length=150)
    Date =models.DateField(auto_now=True)
    Slug =models.SlugField(unique=True)
    Content =models.TextField(validators=[MinLengthValidator(10)])    
    Author =models.ForeignKey(Author,on_delete=models.SET_NULL, null = True, related_name="post" )  
    Tags = models.ManyToManyField(Tag)
     
    def __str__(self) -> str:
        return f"{self.Title} {self.Excerpt} {self.Image_name} {self.Date} {self.Slug} {self.Content} {self.Tags}"
    
    
    