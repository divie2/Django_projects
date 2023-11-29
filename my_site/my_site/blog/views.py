from datetime import date
from django.shortcuts import render

# Create your views here.
all_posts = [
    
    {
        "slug":"hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Divine",
        "date": date(2023, 5, 20),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains!! and i wasnt prepared for what happened whilst hiking.",
        "content": """
                            Qui enim voluptate consectetur commodo excepteur adipisicing culpa irure enim aliquip anim ut. 
                    Nostrud proident magna sit consequat excepteur anim velit labore. 
                    Aliqua esse non eu cillum irure eu dolore est fugiat proident nulla proident ipsum. 
                    Commodo exercitation cillum ullamco velit sit velit ex ut irure nulla culpa.
                    
                    
                    
                    Qui enim voluptate consectetur commodo excepteur adipisicing culpa irure enim aliquip anim ut. 
                    Nostrud proident magna sit consequat excepteur anim velit labore. 
                    Aliqua esse non eu cillum irure eu dolore est fugiat proident nulla proident ipsum. 
                    Commodo exercitation cillum ullamco velit sit velit ex ut irure nulla culpa.
                    
                    
                    Qui enim voluptate consectetur commodo excepteur adipisicing culpa irure enim aliquip anim ut. 
                    Nostrud proident magna sit consequat excepteur anim velit labore. 
                    Aliqua esse non eu cillum irure eu dolore est fugiat proident nulla proident ipsum. 
                    Commodo exercitation cillum ullamco velit sit velit ex ut irure nulla culpa.
                    
            """
    },
     {
        "slug":"coding-to-the-moon",
        "image": "coding.jpg",
        "author": "Divine",
        "date": date(2023, 8, 27),
        "title": "Coding King",
        "excerpt": "Code dragon and i had a little coding battle.",
        "content": """
                            Qui enim voluptate consectetur commodo excepteur adipisicing culpa irure enim aliquip anim ut. 
                    Nostrud proident magna sit consequat excepteur anim velit labore. 
                    Aliqua esse non eu cillum irure eu dolore est fugiat proident nulla proident ipsum. 
                    Commodo exercitation cillum ullamco velit sit velit ex ut irure nulla culpa.
                    
                    
                    
                    Qui enim voluptate consectetur commodo excepteur adipisicing culpa irure enim aliquip anim ut. 
                    Nostrud proident magna sit consequat excepteur anim velit labore. 
                    Aliqua esse non eu cillum irure eu dolore est fugiat proident nulla proident ipsum. 
                    Commodo exercitation cillum ullamco velit sit velit ex ut irure nulla culpa.
                    
                    
                    Qui enim voluptate consectetur commodo excepteur adipisicing culpa irure enim aliquip anim ut. 
                    Nostrud proident magna sit consequat excepteur anim velit labore. 
                    Aliqua esse non eu cillum irure eu dolore est fugiat proident nulla proident ipsum. 
                    Commodo exercitation cillum ullamco velit sit velit ex ut irure nulla culpa.
                    
            """
    },

 {
        "slug":"divine-man",
        "image": "woods.jpg",
        "author": "Divine",
        "date": date(2023, 7, 20),
        "title": "Wood Hiking",
        "excerpt": "I was not prepared ",
        "content": """
                            Qui enim voluptate consectetur commodo excepteur adipisicing culpa irure enim aliquip anim ut. 
                    Nostrud proident magna sit consequat excepteur anim velit labore. 
                    Aliqua esse non eu cillum irure eu dolore est fugiat proident nulla proident ipsum. 
                    Commodo exercitation cillum ullamco velit sit velit ex ut irure nulla culpa.
                    
                    
                    
                    Qui enim voluptate consectetur commodo excepteur adipisicing culpa irure enim aliquip anim ut. 
                    Nostrud proident magna sit consequat excepteur anim velit labore. 
                    Aliqua esse non eu cillum irure eu dolore est fugiat proident nulla proident ipsum. 
                    Commodo exercitation cillum ullamco velit sit velit ex ut irure nulla culpa.
                    
                    
                    Qui enim voluptate consectetur commodo excepteur adipisicing culpa irure enim aliquip anim ut. 
                    Nostrud proident magna sit consequat excepteur anim velit labore. 
                    Aliqua esse non eu cillum irure eu dolore est fugiat proident nulla proident ipsum. 
                    Commodo exercitation cillum ullamco velit sit velit ex ut irure nulla culpa.
                    
            """
    }
 ]
def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    sorted_posts = sorted(all_posts, key=get_date)
    # print(sorted_posts)
    return render(request, "blog/all-post.html", {
        "al_posts": sorted_posts
       
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request , "blog/post-detail.html" , {
        "post" : identified_post
    })