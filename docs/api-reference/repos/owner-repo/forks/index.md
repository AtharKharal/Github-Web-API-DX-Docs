# forks

API endpoints for forks.

## Endpoints


### [List forks](list-forks.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/forks?sort=newest&per_page=30&page=1`

...


### [Create a fork](create-a-fork.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/forks`

Create a fork for the authenticated user.

**Note**: Forking a Repository happens asynchronously. Yo...

