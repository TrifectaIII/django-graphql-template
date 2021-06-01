# Query Examples
## A simple query to fetch model information
```
query simpleQuery {
  allBooks {
    id
    name
    price
  }
}
```
## A query to fetch model information with related models attached
```
query relatedQuery {
  allBooks {
    id
    name
    price
    author {
        id
    }
    genre {
        name
    }
  }
}
```
## A query with an argument to fetch a specific object
```
query argumentQuery {
  bookById(id: 3) {
    name
    author {
      name
    }
  }
}
```
## A query fetching deeper related models
```
query deepQuery {
  allGenres {
    name
    books {
      name
      author {
        name
      }
    }
  }
}
```
## A query with a variable parameter, with variable object
```
query variableQuery($myid: ID!) {
  bookById(id: $myid) {
    name
    genre {
      name
    }
  }
}
```
```
{
  "myid": 1
}
```
## A query which uses aliases to query more than one model
```
query aliasQuery {
  mybook1: bookById(id: 1) {
    name
    genre {
      name
    }
  }
  mybook2: bookById(id: 2) {
    name
    genre {
      name
    }
  }
}
```
## Not Covered
Fragments

Directives