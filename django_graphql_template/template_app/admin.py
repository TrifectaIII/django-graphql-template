from django.contrib import admin
import django_graphql_template.template_app.models as models

# Register models for the admin site

# Change admin site header and title
admin.site.site_header = 'Placeholder Header'
admin.site.site_title = 'Placeholder Title'
admin.site.index_title = 'Placeholder Title'


@admin.register(models.Genre)
class GenreAmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(models.Book)
class BookAmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'author', 'genre']
    list_filter = ['author', 'genre']
    search_fields = ['name']

