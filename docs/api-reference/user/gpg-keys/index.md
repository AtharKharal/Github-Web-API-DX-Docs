# gpg keys

API endpoints for gpg keys.

## Endpoints


### [{gpg key id}](gpg-key-id/index.md)

`` ``




### [List GPG keys for the authenticated user](list-gpg-keys-for-the-authenticated-user.md)

`GET` `{{baseUrl}}/user/gpg_keys?per_page=30&page=1`

Lists the current user's GPG keys. Requires that you are authenticated via Basic Auth or via OAuth w...


### [Create a GPG key for the authenticated user](create-a-gpg-key-for-the-authenticated-user.md)

`POST` `{{baseUrl}}/user/gpg_keys`

Adds a GPG key to the authenticated user's GitHub account. Requires that you are authenticated via B...

