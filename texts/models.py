from django.db import models
from django.utils import timezone
from django.urls import reverse
import datetime
from tinymce import HTMLField
from django_countries.fields import CountryField

class Owner(models.Model):
	owner_name = models.CharField(max_length=200)
	owner_original_name = models.CharField(max_length=200, blank=True)
	owner_description = models.CharField(max_length=500)
	owner_url = models.URLField(max_length=200)
	owner_slug = models.SlugField(max_length=250)
	owner_image = models.ImageField(null=True, blank=True, upload_to='owner_images')
	owner_image_credit = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return self.owner_name

	class Meta:
		ordering = ('owner_name',)

	def get_absolute_url(self):
		return reverse('texts:owner_view', args=[self.owner_slug, self.id])

class Author(models.Model):
	author_last_name = models.CharField(max_length=200)
	author_full_name = models.CharField(max_length=200)
	author_original_full_name = models.CharField(max_length=200, blank=True)
	author_bio = HTMLField()
	author_slug = models.SlugField(max_length=250)
	author_image = models.ImageField(null=True, blank=True, upload_to='author_images')
	author_image_credit = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return self.author_last_name

	def get_absolute_url(self):
		return reverse('texts:author_view', args=[self.author_slug, self.id])

class Theme(models.Model):
	theme_name = models.CharField(max_length=100)
	theme_slug = models.SlugField(max_length=100)
	theme_image = models.ImageField(null=True, blank=True, upload_to='theme_images')
	theme_image_credit = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return self.theme_name

	def get_absolute_url(self):
		return reverse('texts:theme_view', args=[self.theme_slug, self.id])

class Text(models.Model):
	text_title = models.CharField(max_length=200)
	text_original_title = models.CharField(max_length=200, blank=True)
	text_date = models.DateField(default=datetime.date.today)
	text_owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='owner_texts')
	text_author = models.ManyToManyField(Author)
	text_country = CountryField()
	text_themes = models.ManyToManyField(Theme)
	text_summary = models.TextField()
	text_image = models.ImageField(null=True, blank=True, upload_to='text_images')
	text_image_credit = models.CharField(max_length=50, blank=True)
	text_slug = models.SlugField(max_length=250)
	text_original = HTMLField('Original')
	text_translation = HTMLField('Translation')
	text_url = models.URLField(max_length=500)
	text_featured = models.BooleanField()
	text_publish = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('-text_publish',)

	def __str__(self):
		return self.text_title

	def get_absolute_url(self):
		return reverse('texts:text_view', args=[self.text_slug, self.id])