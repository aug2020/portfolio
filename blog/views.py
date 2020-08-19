from django.shortcuts import render ,get_object_or_404
from .models import Blog
# Create your views here.
def all_blogs(request):

    blog = Blog.objects.all()
    return render(request,'blog/all_blogs.html',{'blogs':blog})
def detail(request,blog_id):
    #here were going to grab the blog based on the blog id using the get_object_or_404 module

    blog = get_object_or_404(Blog,pk=blog_id)

    #pk is short for primary key
    #so pk is the id of the blog post in the model, so if there is a primary key that relates to the blogid given to the user then it will show the blog else it will show a 404 page

    return render(request,'blog/detail.html',{'blog':blog})