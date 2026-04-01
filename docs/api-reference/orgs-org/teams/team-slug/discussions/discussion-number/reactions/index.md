# reactions

API endpoints for reactions.

## Endpoints


### [List reactions for a team discussion](list-reactions-for-a-team-discussion.md)

`GET` `{{baseUrl}}/orgs/:org/teams/:team_slug/discussions/:discussion_number/reactions?content=<string>&per_page=30&page=1`

List the reactions to a [team discussion](https://developer.github.com/v3/teams/discussions/). OAuth...


### [Create reaction for a team discussion](create-reaction-for-a-team-discussion.md)

`POST` `{{baseUrl}}/orgs/:org/teams/:team_slug/discussions/:discussion_number/reactions`

Create a reaction to a [team discussion](https://developer.github.com/v3/teams/discussions/). OAuth ...


### [Delete team discussion reaction](delete-team-discussion-reaction.md)

`DELETE` `{{baseUrl}}/orgs/:org/teams/:team_slug/discussions/:discussion_number/reactions/:reaction_id`

**Note:** You can also specify a team or organization with `team_id` and `org_id` using the route `D...

