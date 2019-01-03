from django.contrib import admin

from .models import Owner, Author, Text

admin.site.register(Owner)
admin.site.register(Author)

@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
	list_display = ('text_title', 'text_slug', 'text_owner', 'text_summary',)
	list_filter = ('text_date',)
	search_fields = ('text_title', 'text_summary', 'text_translation')
	prepopulated_fields = {'text_slug': ('text_title',)}
	raw_id_fields = ('text_owner',)
	date_hierarchy = 'text_publish'
	ordering = ('text_date',)