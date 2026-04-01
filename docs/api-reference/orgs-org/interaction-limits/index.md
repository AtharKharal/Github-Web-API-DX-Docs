# interaction-limits

API endpoints for interaction-limits.

## Endpoints


### [Get interaction restrictions for an organization](get-interaction-restrictions-for-an-organization.md)

`GET` `{{baseUrl}}/orgs/:org/interaction-limits`

Shows which group of GitHub users can interact with this organization and when the restriction expir...


### [Set interaction restrictions for an organization](set-interaction-restrictions-for-an-organization.md)

`PUT` `{{baseUrl}}/orgs/:org/interaction-limits`

Temporarily restricts interactions to certain GitHub users in any public repository in the given org...


### [Remove interaction restrictions for an organization](remove-interaction-restrictions-for-an-organization.md)

`DELETE` `{{baseUrl}}/orgs/:org/interaction-limits`

Removes all interaction restrictions from public repositories in the given organization. You must be...

