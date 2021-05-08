import graphene
from graphene_django import DjangoObjectType
import django_graphql_template.template_app.models as templateModels


class TemplateCategoryType(DjangoObjectType):
    class Meta:
        model = templateModels.TemplateCategory
        fields = ['id', 'name', 'objects']

class TemplateObjectType(DjangoObjectType):
    class Meta:
        model = templateModels.TemplateObject
        fields = ['id', 'name', 'price', 'category']

class Query(graphene.ObjectType):
    all_objects = graphene.List(TemplateObjectType)
    category_by_name = graphene.Field(TemplateCategoryType, name=graphene.String(required=True))

    def resolve_all_objects(root, info):
        return templateModels.TemplateObject.objects.select_related('category').all()

    def resolve_category_by_name(root, info, name):
        try:
            return templateModels.TemplateCategory.objects.get(name=name)
        except templateModels.TemplateCategory.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)