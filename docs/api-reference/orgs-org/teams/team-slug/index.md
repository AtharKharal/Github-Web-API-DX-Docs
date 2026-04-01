# {team slug}

API endpoints for {team slug}.

## Endpoints


### [discussions](discussions/index.md)

`` ``




### [memberships/{username}](memberships-username/index.md)

`` ``




### [projects](projects/index.md)

`` ``




### [repos](repos/index.md)

`` ``




### [team-sync/group-mappings](team-sync-group-mappings/index.md)

`` ``




### [Get a team by name](get-a-team-by-name.md)

`GET` `{{baseUrl}}/orgs/:org/teams/:team_slug`

Gets a team using the team's `slug`. GitHub generates the `slug` from the team `name`.

**Note:** Yo...


### [Update a team](update-a-team.md)

`PATCH` `{{baseUrl}}/orgs/:org/teams/:team_slug`

To edit a team, the authenticated user must either be an organization owner or a team maintainer.

*...


### [Delete a team](delete-a-team.md)

`DELETE` `{{baseUrl}}/orgs/:org/teams/:team_slug`

To delete a team, the authenticated user must be an organization owner or team maintainer.

If you a...


### [List pending team invitations](list-pending-team-invitations.md)

`GET` `{{baseUrl}}/orgs/:org/teams/:team_slug/invitations?per_page=30&page=1`

The return hash contains a `role` field which refers to the Organization Invitation role and will be...


### [List team members](list-team-members.md)

`GET` `{{baseUrl}}/orgs/:org/teams/:team_slug/members?role=all&per_page=30&page=1`

Team members will include the members of child teams.

To list members in a team, the team must be v...


### [List child teams](list-child-teams.md)

`GET` `{{baseUrl}}/orgs/:org/teams/:team_slug/teams?per_page=30&page=1`

Lists the child teams of the team specified by `{team_slug}`.

**Note:** You can also specify a team...

