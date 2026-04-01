# reactions

API endpoints for reactions.

## Endpoints


### [List reactions for an issue](list-reactions-for-an-issue.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/issues/:issue_number/reactions?content=<string>&per_page=30&page=1`

List the reactions to an [issue](https://developer.github.com/v3/issues/)....


### [Create reaction for an issue](create-reaction-for-an-issue.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/issues/:issue_number/reactions`

Create a reaction to an [issue](https://developer.github.com/v3/issues/). A response with a `Status:...


### [Delete an issue reaction](delete-an-issue-reaction.md)

`DELETE` `{{baseUrl}}/repos/:owner/:repo/issues/:issue_number/reactions/:reaction_id`

**Note:** You can also specify a repository by `repository_id` using the route `DELETE /repositories...

