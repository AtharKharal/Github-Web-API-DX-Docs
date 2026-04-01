# reactions

API endpoints for reactions.

## Endpoints


### [List reactions for an issue comment](list-reactions-for-an-issue-comment.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/issues/comments/:comment_id/reactions?content=<string>&per_page=30&page=1`

List the reactions to an [issue comment](https://developer.github.com/v3/issues/comments/)....


### [Create reaction for an issue comment](create-reaction-for-an-issue-comment.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/issues/comments/:comment_id/reactions`

Create a reaction to an [issue comment](https://developer.github.com/v3/issues/comments/). A respons...


### [Delete an issue comment reaction](delete-an-issue-comment-reaction.md)

`DELETE` `{{baseUrl}}/repos/:owner/:repo/issues/comments/:comment_id/reactions/:reaction_id`

**Note:** You can also specify a repository by `repository_id` using the route `DELETE delete /repos...

