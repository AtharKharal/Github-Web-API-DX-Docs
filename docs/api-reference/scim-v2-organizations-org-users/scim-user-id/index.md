# {scim user id}

API endpoints for {scim user id}.

## Endpoints


### [Get SCIM provisioning information for a user](get-scim-provisioning-information-for-a-user.md)

`GET` `{{baseUrl}}/scim/v2/organizations/:org/Users/:scim_user_id`

...


### [Update a provisioned organization membership](update-a-provisioned-organization-membership.md)

`PUT` `{{baseUrl}}/scim/v2/organizations/:org/Users/:scim_user_id`

Replaces an existing provisioned user's information. You must provide all the information required f...


### [Update an attribute for a SCIM user](update-an-attribute-for-a-scim-user.md)

`PATCH` `{{baseUrl}}/scim/v2/organizations/:org/Users/:scim_user_id`

Allows you to change a provisioned user's individual attributes. To change a user's values, you must...


### [Delete a SCIM user from an organization](delete-a-scim-user-from-an-organization.md)

`DELETE` `{{baseUrl}}/scim/v2/organizations/:org/Users/:scim_user_id`

...

