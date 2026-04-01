# {secret name}

API endpoints for {secret name}.

## Endpoints


### [repositories](repositories/index.md)

`` ``




### [Get an organization secret](get-an-organization-secret.md)

`GET` `{{baseUrl}}/orgs/:org/actions/secrets/:secret_name`

Gets a single organization secret without revealing its encrypted value. You must authenticate using...


### [Create or update an organization secret](create-or-update-an-organization-secret.md)

`PUT` `{{baseUrl}}/orgs/:org/actions/secrets/:secret_name`

Creates or updates an organization secret with an encrypted value. Encrypt your secret using
[LibSod...


### [Delete an organization secret](delete-an-organization-secret.md)

`DELETE` `{{baseUrl}}/orgs/:org/actions/secrets/:secret_name`

Deletes a secret in an organization using the secret name. You must authenticate using an access tok...

