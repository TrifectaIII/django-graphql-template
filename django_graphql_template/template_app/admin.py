from django.contrib import admin
import django_graphql_template.template_app.models as models

# Register models for the admin site

# Change admin site header and title
admin.site.site_header = 'Placeholder Header'
admin.site.site_title = 'Placeholder Title'
admin.site.index_title = 'Placeholder Title'

@admin.register(models.TemplateCategory)
class TemplateCategoryAmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(models.TemplateObject)
class TemplateObjectAmin(admin.ModelAdmin):
    list_display = ['name','price','template_category']
    list_filter = ['template_category']
    search_fields = ['name']
