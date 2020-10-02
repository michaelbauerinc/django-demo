from django.shortcuts import render
posts = [
    {
        "author": "Mike Bauer",
        "title": "First Post",
        "content": "Hello world!",
        "date_posted": "Oct 2, 2020"
    },
    {
        "author": "Not Mike Bauer",
        "title": "Second Post",
        "content": "Henlo World!",
        "date_posted": "Oct 2, 2020"
    }
]

data = {"title": "About Page"}
def home(request):
    context = {
        "posts": posts
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", data)

# Create your views here.
