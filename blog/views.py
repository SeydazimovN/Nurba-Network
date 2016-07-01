from django.shortcuts import render

# Create your views here.

from django.db.models import Q 

def blog_list(request) :
	return render(request, 'blog/blog.html')
