# invitations

API endpoints for invitations.

## Endpoints


### [List pending organization invitations](list-pending-organization-invitations.md)

`GET` `{{baseUrl}}/orgs/:org/invitations?per_page=30&page=1`

The return hash contains a `role` field which refers to the Organization Invitation role and will be...


### [Create an organization invitation](create-an-organization-invitation.md)

`POST` `{{baseUrl}}/orgs/:org/invitations`

Invite people to an organization by using their GitHub user ID or their email address. In order to c...


### [List organization invitation teams](list-organization-invitation-teams.md)

`GET` `{{baseUrl}}/orgs/:org/invitations/:invitation_id/teams?per_page=30&page=1`

List all teams associated with an invitation. In order to see invitations in an organization, the au...

