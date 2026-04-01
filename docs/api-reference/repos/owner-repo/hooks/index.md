# hooks

API endpoints for hooks.

## Endpoints


### [{hook id}](hook-id/index.md)

`` ``




### [List repository webhooks](list-repository-webhooks.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/hooks?per_page=30&page=1`

...


### [Create a repository webhook](create-a-repository-webhook.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/hooks`

Repositories can have multiple webhooks installed. Each webhook should have a unique `config`. Multi...

