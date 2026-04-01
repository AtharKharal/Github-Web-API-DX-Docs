# comments

API endpoints for comments.

## Endpoints


### [List review comments on a pull request](list-review-comments-on-a-pull-request.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/pulls/:pull_number/comments?sort=created&direction=<string>&since=<string>&per_page=30&page=1`

**Note:** Multi-line comments on pull requests are currently in public beta and subject to change.

...


### [Create a review comment for a pull request](create-a-review-comment-for-a-pull-request.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/pulls/:pull_number/comments`

**Note:** Multi-line comments on pull requests are currently in public beta and subject to change.

...


### [Create a reply for a review comment](create-a-reply-for-a-review-comment.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/pulls/:pull_number/comments/:comment_id/replies`

Creates a reply to a review comment for a pull request. For the `comment_id`, provide the ID of the ...

