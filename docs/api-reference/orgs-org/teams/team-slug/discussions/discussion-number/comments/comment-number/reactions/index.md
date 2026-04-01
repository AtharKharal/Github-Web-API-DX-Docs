# reactions

API endpoints for reactions.

## Endpoints


### [List reactions for a team discussion comment](list-reactions-for-a-team-discussion-comment.md)

`GET` `{{baseUrl}}/orgs/:org/teams/:team_slug/discussions/:discussion_number/comments/:comment_number/reactions?content=<string>&per_page=30&page=1`

List the reactions to a [team discussion comment](https://developer.github.com/v3/teams/discussion_c...


### [Create reaction for a team discussion comment](create-reaction-for-a-team-discussion-comment.md)

`POST` `{{baseUrl}}/orgs/:org/teams/:team_slug/discussions/:discussion_number/comments/:comment_number/reactions`

Create a reaction to a [team discussion comment](https://developer.github.com/v3/teams/discussion_co...


### [Delete team discussion comment reaction](delete-team-discussion-comment-reaction.md)

`DELETE` `{{baseUrl}}/orgs/:org/teams/:team_slug/discussions/:discussion_number/comments/:comment_number/reactions/:reaction_id`

**Note:** You can also specify a team or organization with `team_id` and `org_id` using the route `D...

