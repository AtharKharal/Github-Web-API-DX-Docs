# user

API endpoints for user.

## Endpoints


### [blocks](blocks/index.md)

`` ``




### [emails](emails/index.md)

`` ``




### [following](following/index.md)

`` ``




### [gpg keys](gpg-keys/index.md)

`` ``




### [installations](installations/index.md)

`` ``




### [keys](keys/index.md)

`` ``




### [marketplace purchases](marketplace-purchases/index.md)

`` ``




### [memberships/orgs](memberships-orgs/index.md)

`` ``




### [migrations](migrations/index.md)

`` ``




### [repos](repos/index.md)

`` ``




### [repository invitations](repository-invitations/index.md)

`` ``




### [starred](starred/index.md)

`` ``




### [Get the authenticated user](get-the-authenticated-user.md)

`GET` `{{baseUrl}}/user`

If the authenticated user is authenticated through basic authentication or OAuth with the `user` sco...


### [Update the authenticated user](update-the-authenticated-user.md)

`PATCH` `{{baseUrl}}/user`

**Note:** If your email is set to private and you send an `email` parameter as part of this request ...


### [Set primary email visibility for the authenticated user](set-primary-email-visibility-for-the-authenticated-user.md)

`PATCH` `{{baseUrl}}/user/email/visibility`

Sets the visibility for your primary email addresses....


### [List followers of the authenticated user](list-followers-of-the-authenticated-user.md)

`GET` `{{baseUrl}}/user/followers?per_page=30&page=1`

Lists the people following the authenticated user....


### [List user account issues assigned to the authenticated user](list-user-account-issues-assigned-to-the-authenticated-user.md)

`GET` `{{baseUrl}}/user/issues?filter=assigned&state=open&labels=<string>&sort=created&direction=desc&since=<string>&per_page=30&page=1`

List issues across owned and member repositories assigned to the authenticated user.

**Note**: GitH...


### [List organizations for the authenticated user](list-organizations-for-the-authenticated-user.md)

`GET` `{{baseUrl}}/user/orgs?per_page=30&page=1`

List organizations for the authenticated user.

**OAuth scope requirements**

This only lists organi...


### [Create a user project](create-a-user-project.md)

`POST` `{{baseUrl}}/user/projects`

...


### [List public email addresses for the authenticated user](list-public-email-addresses-for-the-authenticated-user.md)

`GET` `{{baseUrl}}/user/public_emails?per_page=30&page=1`

Lists your publicly visible email address, which you can set with the [Set primary email visibility ...


### [List repositories watched by the authenticated user](list-repositories-watched-by-the-authenticated-user.md)

`GET` `{{baseUrl}}/user/subscriptions?per_page=30&page=1`

Lists repositories the authenticated user is watching....


### [List teams for the authenticated user](list-teams-for-the-authenticated-user.md)

`GET` `{{baseUrl}}/user/teams?per_page=30&page=1`

List all of the teams across all of the organizations to which the authenticated user belongs. This ...

