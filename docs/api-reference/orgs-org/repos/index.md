# repos

API endpoints for repos.

## Endpoints


### [List organization repositories](list-organization-repositories.md)

`GET` `{{baseUrl}}/orgs/:org/repos?type=<string>&sort=created&direction=<string>&per_page=30&page=1`

Lists repositories for the specified organization....


### [Create an organization repository](create-an-organization-repository.md)

`POST` `{{baseUrl}}/orgs/:org/repos`

Creates a new repository in the specified organization. The authenticated user must be a member of t...

