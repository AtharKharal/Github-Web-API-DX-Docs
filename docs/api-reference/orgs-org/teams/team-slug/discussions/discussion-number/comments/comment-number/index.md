# {comment number}

API endpoints for {comment number}.

## Endpoints


### [reactions](reactions/index.md)

`` ``




### [Get a discussion comment](get-a-discussion-comment.md)

`GET` `{{baseUrl}}/orgs/:org/teams/:team_slug/discussions/:discussion_number/comments/:comment_number`

Get a specific comment on a team discussion. OAuth access tokens require the `read:discussion` [scop...


### [Update a discussion comment](update-a-discussion-comment.md)

`PATCH` `{{baseUrl}}/orgs/:org/teams/:team_slug/discussions/:discussion_number/comments/:comment_number`

Edits the body text of a discussion comment. OAuth access tokens require the `write:discussion` [sco...


### [Delete a discussion comment](delete-a-discussion-comment.md)

`DELETE` `{{baseUrl}}/orgs/:org/teams/:team_slug/discussions/:discussion_number/comments/:comment_number`

Deletes a comment on a team discussion. OAuth access tokens require the `write:discussion` [scope](h...

