# reactions

API endpoints for reactions.

## Endpoints


### [List reactions for a pull request review comment](list-reactions-for-a-pull-request-review-comment.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/pulls/comments/:comment_id/reactions?content=<string>&per_page=30&page=1`

List the reactions to a [pull request review comment](https://developer.github.com/v3/pulls/comments...


### [Create reaction for a pull request review comment](create-reaction-for-a-pull-request-review-comment.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/pulls/comments/:comment_id/reactions`

Create a reaction to a [pull request review comment](https://developer.github.com/v3/pulls/comments/...


### [Delete a pull request comment reaction](delete-a-pull-request-comment-reaction.md)

`DELETE` `{{baseUrl}}/repos/:owner/:repo/pulls/comments/:comment_id/reactions/:reaction_id`

**Note:** You can also specify a repository by `repository_id` using the route `DELETE /repositories...

