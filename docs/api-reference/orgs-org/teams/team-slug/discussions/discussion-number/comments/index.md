# comments

API endpoints for comments.

## Endpoints


### [{comment number}](comment-number/index.md)

`` ``




### [List discussion comments](list-discussion-comments.md)

`GET` `{{baseUrl}}/orgs/:org/teams/:team_slug/discussions/:discussion_number/comments?direction=desc&per_page=30&page=1`

List all comments on a team discussion. OAuth access tokens require the `read:discussion` [scope](ht...


### [Create a discussion comment](create-a-discussion-comment.md)

`POST` `{{baseUrl}}/orgs/:org/teams/:team_slug/discussions/:discussion_number/comments`

Creates a new comment on a team discussion. OAuth access tokens require the `write:discussion` [scop...

