from django.urls import path

from .views import HomePageView, TextView, OwnerView, AuthorView, TextListView, OwnerListView, AuthorListView, ThemeView, CountryView

app_name = 'texts'

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('texts/', TextListView.as_view(), name='text_list'),
	path('texts/<slug:text_slug>,<int:pk>/', TextView.as_view(), name='text_view'),
	path('publishers/', OwnerListView.as_view(), name='owner_list'),
	path('publishers/<slug:owner_slug>,<int:pk>/', OwnerView.as_view(), name='owner_view'),
	path('authors/', AuthorListView.as_view(), name='author_list'),
	path('authors/<slug:author_slug>,<int:pk>/', AuthorView.as_view(), name='author_view'),
	path('topics/<slug:theme_slug>,<int:pk>/', ThemeView.as_view(), name='theme_view'),
	path('countries/<slug:country_slug>,<int:pk>/', CountryView.as_view(), name='country_view'),
]