import graphene
from graphene_django import DjangoObjectType
import django_graphql_template.template_app.models as models

# Define GraphQL Schema for this app


# Define types for models
class TemplateCategoryType(DjangoObjectType):
    class Meta:
        model = models.TemplateCategory
        fields = ['id', 'name', 'template_objects']

class TemplateObjectType(DjangoObjectType):
    class Meta:
        model = models.TemplateObject
        fields = ['id', 'name', 'price', 'category']


# Define query fields
class Query(graphene.ObjectType):

    # fetch all objects
    all_objects = graphene.List(TemplateObjectType)
    def resolve_all_objects(root, info):
        return models.TemplateObject.objects.select_related('category').all()

    # fetch a category given a specific id
    object_by_id = graphene.Field(TemplateCategoryType, id=graphene.Int(required=False))
    def resolve_object_by_id(root, info, id):
        try:
            return models.TemplateObject.objects.get(id=id)
        except models.TemplateObject.DoesNotExist:
            return None

    # fetch all categories
    all_categories = graphene.List(TemplateCategoryType)
    def resolve_all_categories(root, info):
        return models.TemplateObject.objects.select_related('objects').all()

    # fetch a category given a specific name 
    category_by_name = graphene.Field(TemplateCategoryType, name=graphene.String(required=False))
    def resolve_category_by_name(root, info, name):
        try:
            return models.TemplateCategory.objects.get(name=name)
        except models.TemplateCategory.DoesNotExist:
            return None


# Define mutation fields