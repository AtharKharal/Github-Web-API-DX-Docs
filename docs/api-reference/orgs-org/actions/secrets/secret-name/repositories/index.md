# repositories

API endpoints for repositories.

## Endpoints


### [{repository id}](repository-id/index.md)

`` ``




### [List selected repositories for an organization secret](list-selected-repositories-for-an-organization-secret.md)

`GET` `{{baseUrl}}/orgs/:org/actions/secrets/:secret_name/repositories`

Lists all repositories that have been selected when the `visibility` for repository access to a secr...


### [Set selected repositories for an organization secret](set-selected-repositories-for-an-organization-secret.md)

`PUT` `{{baseUrl}}/orgs/:org/actions/secrets/:secret_name/repositories`

Replaces all repositories for an organization secret when the `visibility` for repository access is ...

