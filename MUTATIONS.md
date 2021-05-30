# Mutation Examples
## A mutation which creates a new object
```
mutation createMutation {
  newBook (name: "MyBook", authorId: 1, genreId: 1, price: 100) {
    book {
      id
    }
  }
}
```
## A mutation which changes an existing object
```
mutation updateMutation {
  updateBook (id: 7, price: 1) {
    book {
      id
      name
      price
    }
  }
}
```