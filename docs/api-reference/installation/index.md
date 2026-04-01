# installation

API endpoints for installation.

## Endpoints


### [List repositories accessible to the app installation](list-repositories-accessible-to-the-app-installation.md)

`GET` `{{baseUrl}}/installation/repositories?per_page=30&page=1`

List repositories that an app installation can access.

You must use an [installation access token](...


### [Revoke an installation access token](revoke-an-installation-access-token.md)

`DELETE` `{{baseUrl}}/installation/token`

Revokes the installation token you're using to authenticate as an installation and access this endpo...

