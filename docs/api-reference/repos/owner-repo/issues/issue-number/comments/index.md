# comments

API endpoints for comments.

## Endpoints


### [List issue comments](list-issue-comments.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/issues/:issue_number/comments?since=<string>&per_page=30&page=1`

Issue Comments are ordered by ascending ID....


### [Create an issue comment](create-an-issue-comment.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/issues/:issue_number/comments`

This endpoint triggers [notifications](https://help.github.com/articles/about-notifications/). Creat...

