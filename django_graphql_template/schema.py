import graphene
import django_graphql_template.template_app.schema as template_app_schema

# Combine GraphQL Schema from different apps

class Query(
    template_app_schema.Query,
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query)
