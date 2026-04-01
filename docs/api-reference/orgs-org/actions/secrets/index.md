# secrets

API endpoints for secrets.

## Endpoints


### [{secret name}](secret-name/index.md)

`` ``




### [List organization secrets](list-organization-secrets.md)

`GET` `{{baseUrl}}/orgs/:org/actions/secrets?per_page=30&page=1`

Lists all secrets available in an organization without revealing their encrypted values. You must au...


### [Get an organization public key](get-an-organization-public-key.md)

`GET` `{{baseUrl}}/orgs/:org/actions/secrets/public-key`

Gets your public key, which you need to encrypt secrets. You need to encrypt a secret before you can...

