from django.shortcuts import render


# Create your views here.

posts = [{
    'author': 'John Doe',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'April 20, 2024'
    },
    
    {
    'author': 'Jane Smith',
    'title': 'Blog Post 2', 
    'content': 'Second post content',
    'date_posted': 'April 21, 2024'
    },

    {
    'author': 'Alice Johnson',
    'title': 'Blog Post 3', 
    'content': 'Third post content',
    'date_posted': 'April 22, 2024'
    }
    ]

def home(request):
    context = {
        'posts': posts,
        'title': 'home Page',
    }
    return render(request, "blog/home.html", context)   

def about(request):
    return render(request, "blog/about.html", {'title': 'About Page'})   

def contact(request):
    return render(request, "blog/contact.html")