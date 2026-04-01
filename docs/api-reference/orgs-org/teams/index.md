# teams

API endpoints for teams.

## Endpoints


### [{team slug}](team-slug/index.md)

`` ``




### [List teams](list-teams.md)

`GET` `{{baseUrl}}/orgs/:org/teams?per_page=30&page=1`

Lists all teams in an organization that are visible to the authenticated user....


### [Create a team](create-a-team.md)

`POST` `{{baseUrl}}/orgs/:org/teams`

To create a team, the authenticated user must be a member or owner of `{org}`. By default, organizat...

