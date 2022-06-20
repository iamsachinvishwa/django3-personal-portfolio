from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    blog = Blog.objects.order_by()
    return render(request, 'blog/all_blogs.html', {'all_blogs': blog})


def detail(request, blog_id):
    blog1 = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog': blog1})