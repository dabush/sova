from django.contrib import admin

from .models import Owner, Author, Text, Theme

admin.site.register(Owner)
admin.site.register(Author)
admin.site.register(Theme)

@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'owner', 'summary',)
	list_filter = ('date',)
	search_fields = ('title', 'summary', 'text_translation')
	prepopulated_fields = {'slug': ('title',)}
	raw_id_fields = ('owner',)
	date_hierarchy = 'publish'
	ordering = ('date',)