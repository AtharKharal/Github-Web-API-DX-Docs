# token

API endpoints for token.

## Endpoints


### [Check a token](check-a-token.md)

`POST` `{{baseUrl}}/applications/:client_id/token`

OAuth applications can use a special API method for checking OAuth token validity without exceeding ...


### [Reset a token](reset-a-token.md)

`PATCH` `{{baseUrl}}/applications/:client_id/token`

OAuth applications can use this API method to reset a valid OAuth token without end-user involvement...


### [Delete an app token](delete-an-app-token.md)

`DELETE` `{{baseUrl}}/applications/:client_id/token`

OAuth application owners can revoke a single token for an OAuth application. You must use [Basic Aut...

