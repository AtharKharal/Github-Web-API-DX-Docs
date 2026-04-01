# comments

API endpoints for comments.

## Endpoints


### [List commit comments](list-commit-comments.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/commits/:commit_sha/comments?per_page=30&page=1`

Use the `:commit_sha` to specify the commit that will have its comments listed....


### [Create a commit comment](create-a-commit-comment.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/commits/:commit_sha/comments`

Create a comment for a commit using its `:commit_sha`.

This endpoint triggers [notifications](https...

