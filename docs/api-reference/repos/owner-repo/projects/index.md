# projects

API endpoints for projects.

## Endpoints


### [List repository projects](list-repository-projects.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/projects?state=open&per_page=30&page=1`

Lists the projects in a repository. Returns a `404 Not Found` status if projects are disabled in the...


### [Create a repository project](create-a-repository-project.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/projects`

Creates a repository project board. Returns a `404 Not Found` status if projects are disabled in the...

