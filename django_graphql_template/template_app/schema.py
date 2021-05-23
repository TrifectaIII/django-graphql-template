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
        fields = ['id', 'name', 'price', 'template_category']


# Define query fields
class Query(graphene.ObjectType):

    # fetch all objects
    all_objects = graphene.List(TemplateObjectType)
    def resolve_all_objects(root, info):
        return models.TemplateObject.objects.select_related('template_category').all()

    # fetch a category given a specific id
    object_by_id = graphene.Field(TemplateCategoryType, id=graphene.ID(required=True))
    def resolve_object_by_id(root, info, id):
        try:
            return models.TemplateObject.objects.get(id=id)
        except models.TemplateObject.DoesNotExist:
            return None

    # fetch all categories
    all_categories = graphene.List(TemplateCategoryType)
    def resolve_all_categories(root, info):
        return models.TemplateObject.objects.select_related('template_objects').all()

    # fetch a category given a specific name 
    category_by_name = graphene.Field(TemplateCategoryType, name=graphene.String(required=True))
    def resolve_category_by_name(root, info, name):
        try:
            return models.TemplateCategory.objects.get(name=name)
        except models.TemplateCategory.DoesNotExist:
            return None


# Define mutation fields
class UpdateObjectMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        price = graphene.Int(required=False)
        name = graphene.String(required=False)
        category_id = graphene.ID(required=False)
    
    template_object = graphene.Field(TemplateObjectType)

    @classmethod
    def mutate(cls, root, info, id, price=False, name=False, category_id=False):
        template_object = models.TemplateObject.objects.get(id=id)
        template_object.price = price or template_object.price
        template_object.name = name or template_object.name
        template_object.template_category_id = category_id or template_object.template_category_id
        template_object.save()
        return UpdateObjectMutation(template_object=template_object)

class NewObjectMutation(graphene.Mutation):
    class Arguments:
        price = graphene.Int(required=True)
        name = graphene.String(required=True)
        category_id = graphene.ID(required=True)
    
    template_object = graphene.Field(TemplateObjectType)

    @classmethod
    def mutate(cls, root, info, price, name, category_id):
        template_object = models.TemplateObject.objects.create(
            name=name,
            price=price,
            template_category_id=category_id,
        )
        return UpdateObjectMutation(template_object=template_object)

class Mutation(graphene.ObjectType):
    update_object = UpdateObjectMutation.Field()
    new_object = NewObjectMutation.Field()
