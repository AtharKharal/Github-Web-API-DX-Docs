# {secret name}

API endpoints for {secret name}.

## Endpoints


### [Get a repository secret](get-a-repository-secret.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/actions/secrets/:secret_name`

Gets a single repository secret without revealing its encrypted value. You must authenticate using a...


### [Create or update a repository secret](create-or-update-a-repository-secret.md)

`PUT` `{{baseUrl}}/repos/:owner/:repo/actions/secrets/:secret_name`

Creates or updates a repository secret with an encrypted value. Encrypt your secret using
[LibSodium...


### [Delete a repository secret](delete-a-repository-secret.md)

`DELETE` `{{baseUrl}}/repos/:owner/:repo/actions/secrets/:secret_name`

Deletes a secret in a repository using the secret name. You must authenticate using an access token ...

