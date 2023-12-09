from turtle import title
from django.shortcuts import render
from django.http import Http404 
from django.shortcuts import get_object_or_404
from django.db.models import Avg,Max,Min


from .models import Book

# Create your views here.
def index(request):
    books = Book.objects.all()
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    
    
    return render(request,"book_outlet/index.html", 
                  {'book':books,
                   'total_number_of_books': num_books,
                   'average_rating': avg_rating ,
                   })

def book_detail(request, slug):
#    try: 
#     books = Book.objects.get(pk=id)    
#    except:
#     raise Http404() 
        
    books = get_object_or_404(Book, slug=slug)    
    return render(request, 'book_outlet/book_detail.html',
                  {
                      'title':books.title,
                      'is_bestseller': books.is_bestselling,
                      'author': books.author,
                      'rating': books.rating,
                  })