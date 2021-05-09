import graphene
from graphene_django import DjangoObjectType
import django_graphql_template.template_app.models as models

# Define GraphQL Schema for this app

class TemplateCategoryType(DjangoObjectType):
    class Meta:
        model = models.TemplateCategory
        fields = ['id', 'name', 'template_objects']

class TemplateObjectType(DjangoObjectType):
    class Meta:
        model = models.TemplateObject
        fields = ['id', 'name', 'price', 'category']

class Query(graphene.ObjectType):
    all_objects = graphene.List(TemplateObjectType)
    category_by_name = graphene.Field(TemplateCategoryType, name=graphene.String(required=True))

    def resolve_all_objects(root, info):
        return models.TemplateObject.objects.select_related('category').all()

    def resolve_category_by_name(root, info, name):
        try:
            return models.TemplateCategory.objects.get(name=name)
        except models.TemplateCategory.DoesNotExist:
            return None
