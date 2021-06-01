import graphene
from graphene_django import DjangoObjectType
import django_graphql_template.template_app.models as models

# Define GraphQL Schema for this app


# Define types for models
class GenreType(DjangoObjectType):
    class Meta:
        model = models.Genre
        fields = ['id', 'name', 'books']

class AuthorType(DjangoObjectType):
    class Meta:
        model = models.Author
        fields = ['id', 'name', 'books']

class BookType(DjangoObjectType):
    class Meta:
        model = models.Book
        fields = ['id', 'name', 'price', 'author','genre']


# Define query fields
class Query(graphene.ObjectType):

    # fetch all books
    all_books = graphene.List(BookType)
    def resolve_all_books(root, info):
        return models.Book.objects.select_related('genre').select_related('author').all()

    # fetch a book given a specific id
    book_by_id = graphene.Field(BookType, id=graphene.ID(required=True))
    def resolve_book_by_id(root, info, id):
        try:
            return models.Book.objects.select_related('genre').select_related('author').get(id=id)
        except models.Book.DoesNotExist:
            return None

    # fetch all genres
    all_genres = graphene.List(GenreType)
    def resolve_all_genres(root, info):
        return models.Genre.objects.all()

    # fetch a genre given a specific name 
    genre_by_name = graphene.Field(GenreType, name=graphene.String(required=True))
    def resolve_genre_by_name(root, info, name):
        try:
            return models.Genre.objects.get(name=name)
        except models.Genre.DoesNotExist:
            return None

    # fetch all authors
    all_authors = graphene.List(AuthorType)
    def resolve_all_authors(root, info):
        return models.Author.objects.all()

    # fetch an author given a specific name 
    author_by_name = graphene.Field(AuthorType, name=graphene.String(required=True))
    def resolve_author_by_name(root, info, name):
        try:
            return models.Author.objects.get(name=name)
        except models.Author.DoesNotExist:
            return None


# Define mutation fields
class UpdateBookMutation(graphene.Mutation):
    # mutation for updating an existing book
    class Arguments:
        id = graphene.ID(required=True)
        price = graphene.Int(required=False)
        name = graphene.String(required=False)
        author_id = graphene.ID(required=False)
        genre_id = graphene.ID(required=False)
    
    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls, root, info, id, price=False, name=False, author_id=False, genre_id=False):
        book = models.Book.objects.get(id=id)
        book.price = price or book.price
        book.name = name or book.name
        book.author_id = author_id or book.author_id
        book.genre_id = genre_id or book.genre_id
        book.save()
        return UpdateBookMutation(book=book)


class NewBookMutation(graphene.Mutation):
    # mutation for creating a new book
    class Arguments:
        price = graphene.Int(required=True)
        name = graphene.String(required=True)
        author_id = graphene.ID(required=True)
        genre_id = graphene.ID(required=True)
    
    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls, root, info, price, name, author_id, genre_id):
        book = models.Book.objects.create(
            name=name,
            price=price,
            author_id=author_id,
            genre_id=genre_id,
        )
        return NewBookMutation(book=book)


class Mutation(graphene.ObjectType):
    update_book = UpdateBookMutation.Field()
    new_book = NewBookMutation.Field()
