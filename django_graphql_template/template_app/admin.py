from django.contrib import admin
import django_graphql_template.template_app.models as models


@admin.register(models.TemplateObject)
class TemplateObjectAmin(admin.ModelAdmin):
    pass

@admin.register(models.TemplateCategory)
class TemplateCategoryAmin(admin.ModelAdmin):
    pass