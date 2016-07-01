from django.shortcuts import render, get_object_or_404
from .models import Image
from .forms import PostForm

from django.http import HttpResponse, HttpResponseRedirect

def index(request) :
	return render(request, 'personal/home.html')

def contact(request) :
	return render (request, 'personal/basic.html', {'content':['if you would like to contact me, please email me','nurbol.seydazimov@gmail.com']})

def friends(request) :
	return render (request, 'personal/friends.html')
	
def messages(request) :
	return render (request, 'personal/messages.html')

def images(request) :
	queryset = Image.objects.all()
	context = {
		"queryset" : queryset
	}
	return render (request, 'personal/images.html', context)
	
def add_image(request) :
	form = PostForm(request.POST or None)
	if form.is_valid() :
		instance = form.save(commit = False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form" : form
	}
	return render (request, 'personal/add_image.html', context)	
