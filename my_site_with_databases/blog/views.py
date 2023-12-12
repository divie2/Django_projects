from datetime import date
from django.shortcuts import get_object_or_404, render
from .models import Post, Author,Tag

# Create your views here.
all_posts = []
    
    
def get_date(post):
    return post['date']

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-Date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    # sorted_posts = sorted(all_posts, key=get_date)
    sorted_posts = Post.objects.all().order_by("-Date")
    # print(sorted_posts)
    return render(request, "blog/all-post.html", {
        "al_posts": sorted_posts
       
    })

def post_detail(request, slug):
    
    identified_post = get_object_or_404(Post, Slug = slug)
    return render(request , "blog/post-detail.html" , {
        "post" : identified_post,
        "post_tag" : identified_post.Tags.all()
    })