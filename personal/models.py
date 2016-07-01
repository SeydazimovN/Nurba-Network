from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from django.db import models

# Create your models here.

class Image(models.Model):
	title = models.CharField(max_length = 120)
	link = models.CharField(max_length = 120)
	
	def __unicode__(self) :
		return self.title 
	def __str__(self) :
		return self.title
	def get_absolute_url(self) :
		return reverse("images")

