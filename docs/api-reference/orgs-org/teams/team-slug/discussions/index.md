# discussions

API endpoints for discussions.

## Endpoints


### [{discussion number}](discussion-number/index.md)

`` ``




### [List discussions](list-discussions.md)

`GET` `{{baseUrl}}/orgs/:org/teams/:team_slug/discussions?direction=desc&per_page=30&page=1`

List all discussions on a team's page. OAuth access tokens require the `read:discussion` [scope](htt...


### [Create a discussion](create-a-discussion.md)

`POST` `{{baseUrl}}/orgs/:org/teams/:team_slug/discussions`

Creates a new discussion post on a team's page. OAuth access tokens require the `write:discussion` [...

