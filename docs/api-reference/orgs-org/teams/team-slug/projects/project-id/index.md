# {project id}

API endpoints for {project id}.

## Endpoints


### [Check team permissions for a project](check-team-permissions-for-a-project.md)

`GET` `{{baseUrl}}/orgs/:org/teams/:team_slug/projects/:project_id`

Checks whether a team has `read`, `write`, or `admin` permissions for an organization project. The r...


### [Add or update team project permissions](add-or-update-team-project-permissions.md)

`PUT` `{{baseUrl}}/orgs/:org/teams/:team_slug/projects/:project_id`

Adds an organization project to a team. To add a project to a team or update the team's permission o...


### [Remove a project from a team](remove-a-project-from-a-team.md)

`DELETE` `{{baseUrl}}/orgs/:org/teams/:team_slug/projects/:project_id`

Removes an organization project from a team. An organization owner or a team maintainer can remove a...

