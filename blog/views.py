from django.shortcuts import render

posts = [
    {
        'author': 'Devkota Prajwol',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 3, 2020'
    },
    {
        'author': 'Devkota Ashish',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'August 4, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
