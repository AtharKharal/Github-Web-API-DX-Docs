# {discussion number}

API endpoints for {discussion number}.

## Endpoints


### [comments](comments/index.md)

`` ``




### [reactions](reactions/index.md)

`` ``




### [Get a discussion](get-a-discussion.md)

`GET` `{{baseUrl}}/orgs/:org/teams/:team_slug/discussions/:discussion_number`

Get a specific discussion on a team's page. OAuth access tokens require the `read:discussion` [scope...


### [Update a discussion](update-a-discussion.md)

`PATCH` `{{baseUrl}}/orgs/:org/teams/:team_slug/discussions/:discussion_number`

Edits the title and body text of a discussion post. Only the parameters you provide are updated. OAu...


### [Delete a discussion](delete-a-discussion.md)

`DELETE` `{{baseUrl}}/orgs/:org/teams/:team_slug/discussions/:discussion_number`

Delete a discussion from a team's page. OAuth access tokens require the `write:discussion` [scope](h...

