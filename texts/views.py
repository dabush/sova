from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, ListView

from .models import Owner, Author, Text, Theme, Country

class HomePageView(TemplateView):

	template_name = "home.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['latest_texts'] = Text.objects.all()[:5]
		context['featured_texts'] = Text.objects.filter(featured=True)
		context['topics'] = Theme.objects.all()[:10]
		context['countries'] = Country.objects.all()[:10]
		return context

class TextView(DetailView):

	model = Text

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class OwnerView(DetailView):

	model = Owner

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class AuthorView(DetailView):

	model = Author

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class TextListView(ListView):

	model = Text
	paginate_by = 20

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class OwnerListView(ListView):

	model = Owner
	paginate_by = 20

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class CountryView(DetailView):

	model = Country

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class AuthorListView(ListView):

	model = Author
	paginate_by = 20

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class ThemeView(DetailView):

	model = Theme

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class ThemeListView(ListView):

	model = Theme
	paginate_by = 20

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['countries'] = Country.objects.all()
		return context 