# secrets

API endpoints for secrets.

## Endpoints


### [{secret name}](secret-name/index.md)

`` ``




### [List repository secrets](list-repository-secrets.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/actions/secrets?per_page=30&page=1`

Lists all secrets available in a repository without revealing their encrypted values. You must authe...


### [Get a repository public key](get-a-repository-public-key.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/actions/secrets/public-key`

Gets your public key, which you need to encrypt secrets. You need to encrypt a secret before you can...

