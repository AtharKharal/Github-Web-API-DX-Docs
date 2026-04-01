# repos

API endpoints for repos.

## Endpoints


### [List repositories for the authenticated user](list-repositories-for-the-authenticated-user.md)

`GET` `{{baseUrl}}/user/repos?visibility=all&affiliation=owner,collaborator,organization_member&type=all&sort=full_name&direction=<string>&per_page=30&page=1&since=<string>&before=<string>`

Lists repositories that the authenticated user has explicit permission (`:read`, `:write`, or `:admi...


### [Create a repository for the authenticated user](create-a-repository-for-the-authenticated-user.md)

`POST` `{{baseUrl}}/user/repos`

Creates a new repository for the authenticated user.

**OAuth scope requirements**

When using [OAut...

