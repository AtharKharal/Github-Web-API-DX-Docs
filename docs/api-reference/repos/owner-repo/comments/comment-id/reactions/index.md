# reactions

API endpoints for reactions.

## Endpoints


### [List reactions for a commit comment](list-reactions-for-a-commit-comment.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/comments/:comment_id/reactions?content=<string>&per_page=30&page=1`

List the reactions to a [commit comment](https://developer.github.com/v3/repos/comments/)....


### [Create reaction for a commit comment](create-reaction-for-a-commit-comment.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/comments/:comment_id/reactions`

Create a reaction to a [commit comment](https://developer.github.com/v3/repos/comments/). A response...


### [Delete a commit comment reaction](delete-a-commit-comment-reaction.md)

`DELETE` `{{baseUrl}}/repos/:owner/:repo/comments/:comment_id/reactions/:reaction_id`

**Note:** You can also specify a repository by `repository_id` using the route `DELETE /repositories...

