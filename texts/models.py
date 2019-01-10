from django.db import models
from django.utils import timezone
from django.urls import reverse
import datetime
from tinymce import HTMLField

class Owner(models.Model):
	name = models.CharField(max_length=200)
	original_name = models.CharField(max_length=200, blank=True)
	description = models.CharField(max_length=500)
	url = models.URLField(max_length=200)
	slug = models.SlugField(max_length=250)
	image = models.ImageField(null=True, blank=True, upload_to='owner_images')
	image_credit = models.CharField(max_length=50, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)

	def get_absolute_url(self):
		return reverse('texts:owner_view', args=[self.slug, self.id])

class Author(models.Model):
	last_name = models.CharField(max_length=200)
	full_name = models.CharField(max_length=200)
	original_full_name = models.CharField(max_length=200, blank=True)
	bio = HTMLField()
	slug = models.SlugField(max_length=250)
	image = models.ImageField(null=True, blank=True, upload_to='author_images')
	image_credit = models.CharField(max_length=50, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.full_name

	def get_absolute_url(self):
		return reverse('texts:author_view', args=[self.slug, self.id])

class Theme(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	image = models.ImageField(null=True, blank=True, upload_to='theme_images')
	image_credit = models.CharField(max_length=50, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


	class Meta:
		ordering = ('-modified',)

	def get_absolute_url(self):
		return reverse('texts:theme_view', args=[self.slug, self.id])

class Country(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=100)
	image = models.ImageField(null=True, blank=True, upload_to='country_images')
	image_credit = models.CharField(max_length=50, blank=True)
	featured = models.BooleanField()

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)

class Text(models.Model):
	title = models.CharField(max_length=200)
	original_title = models.CharField(max_length=200, blank=True)
	date = models.DateField(default=datetime.date.today)
	owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='owner_texts')
	author = models.ManyToManyField(Author)
	summary = models.TextField()
	themes = models.ManyToManyField(Theme, related_name='themes')
	image = models.ImageField(null=True, blank=True, upload_to='text_images')
	image_credit = models.CharField(max_length=50, blank=True)
	slug = models.SlugField(max_length=250)
	text_original = HTMLField('Original')
	text_translation = HTMLField('Translation')
	url = models.URLField(max_length=500)
	featured = models.BooleanField()
	publish = models.DateTimeField(default=timezone.now)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('texts:text_view', args=[self.slug, self.id])