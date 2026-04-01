# projects

API endpoints for projects.

## Endpoints


### [List organization projects](list-organization-projects.md)

`GET` `{{baseUrl}}/orgs/:org/projects?state=open&per_page=30&page=1`

Lists the projects in an organization. Returns a `404 Not Found` status if projects are disabled in ...


### [Create an organization project](create-an-organization-project.md)

`POST` `{{baseUrl}}/orgs/:org/projects`

Creates an organization project board. Returns a `404 Not Found` status if projects are disabled in ...

