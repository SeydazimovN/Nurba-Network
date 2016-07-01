from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post

from . import views

temp = Post.objects.all().order_by("-date")[:25]
print (temp)
print ("blah blah")
cur = views.blog_list
print cur

# query_name = views.blog_list

# temp = Post.objects.filter(title__icontains = '').order_by("-date")[:25]

urlpatterns = [ url(r'^$', views.blog_list, name = 'blog_list'),
				# url(r'^$', ListView.as_view(queryset = temp, template_name = "blog/blog.html")),
				url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Post, template_name = 'blog/post.html'))]
        
