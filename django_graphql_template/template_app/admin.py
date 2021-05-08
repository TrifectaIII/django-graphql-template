from django.contrib import admin
import django_graphql_template.template_app.models as models

@admin.register(models.TemplateCategory)
class TemplateCategoryAmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(models.TemplateObject)
class TemplateObjectAmin(admin.ModelAdmin):
    list_display = ['name','price','category']
    list_filter = ['category']
    search_fields = ['name']
