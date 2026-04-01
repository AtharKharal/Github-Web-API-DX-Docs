# orgs/{org}

API endpoints for orgs/{org}.

## Endpoints


### [actions](actions/index.md)

`` ``




### [blocks](blocks/index.md)

`` ``




### [credential-authorizations](credential-authorizations/index.md)

`` ``




### [hooks](hooks/index.md)

`` ``




### [interaction-limits](interaction-limits/index.md)

`` ``




### [invitations](invitations/index.md)

`` ``




### [members](members/index.md)

`` ``




### [memberships/{username}](memberships-username/index.md)

`` ``




### [migrations](migrations/index.md)

`` ``




### [outside collaborators](outside-collaborators/index.md)

`` ``




### [projects](projects/index.md)

`` ``




### [public members](public-members/index.md)

`` ``




### [repos](repos/index.md)

`` ``




### [settings/billing](settings-billing/index.md)

`` ``




### [teams](teams/index.md)

`` ``




### [Get an organization](get-an-organization.md)

`GET` `{{baseUrl}}/orgs/:org`

To see many of the organization response values, you need to be an authenticated organization owner ...


### [Update an organization](update-an-organization.md)

`PATCH` `{{baseUrl}}/orgs/:org`

**Parameter Deprecation Notice:** GitHub will replace and discontinue `members_allowed_repository_cr...


### [List public organization events](list-public-organization-events.md)

`GET` `{{baseUrl}}/orgs/:org/events?per_page=30&page=1`

...


### [Get an organization installation for the authenticated app](get-an-organization-installation-for-the-authenticated-app.md)

`GET` `{{baseUrl}}/orgs/:org/installation`

Enables an authenticated GitHub App to find the organization's installation information.

You must u...


### [List app installations for an organization](list-app-installations-for-an-organization.md)

`GET` `{{baseUrl}}/orgs/:org/installations?per_page=30&page=1`

Lists all GitHub Apps in an organization. The installation count includes all GitHub Apps installed ...


### [List organization issues assigned to the authenticated user](list-organization-issues-assigned-to-the-authenticated-user.md)

`GET` `{{baseUrl}}/orgs/:org/issues?filter=assigned&state=open&labels=<string>&sort=created&direction=desc&since=<string>&per_page=30&page=1`

List issues in an organization assigned to the authenticated user.

**Note**: GitHub's REST API v3 c...


### [List IdP groups for an organization](list-idp-groups-for-an-organization.md)

`GET` `{{baseUrl}}/orgs/:org/team-sync/groups?per_page=30&page=1`

Team synchronization is available for organizations using GitHub Enterprise Cloud. For more informat...

