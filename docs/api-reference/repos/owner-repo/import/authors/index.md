# authors

API endpoints for authors.

## Endpoints


### [Get commit authors](get-commit-authors.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/import/authors?since=<string>`

Each type of source control system represents authors in a different way. For example, a Git commit ...


### [Map a commit author](map-a-commit-author.md)

`PATCH` `{{baseUrl}}/repos/:owner/:repo/import/authors/:author_id`

Update an author's identity for the import. Your application can continue updating authors any time ...

