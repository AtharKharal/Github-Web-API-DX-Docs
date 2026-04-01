# {owner}/{repo}

API endpoints for {owner}/{repo}.

## Endpoints


### [Check team permissions for a repository](check-team-permissions-for-a-repository.md)

`GET` `{{baseUrl}}/orgs/:org/teams/:team_slug/repos/:owner/:repo`

Checks whether a team has `admin`, `push`, `maintain`, `triage`, or `pull` permission for a reposito...


### [Add or update team repository permissions](add-or-update-team-repository-permissions.md)

`PUT` `{{baseUrl}}/orgs/:org/teams/:team_slug/repos/:owner/:repo`

To add a repository to a team or update the team's permission on a repository, the authenticated use...


### [Remove a repository from a team](remove-a-repository-from-a-team.md)

`DELETE` `{{baseUrl}}/orgs/:org/teams/:team_slug/repos/:owner/:repo`

If the authenticated user is an organization owner or a team maintainer, they can remove any reposit...

