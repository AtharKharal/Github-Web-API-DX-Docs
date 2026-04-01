# requested reviewers

API endpoints for requested reviewers.

## Endpoints


### [List requested reviewers for a pull request](list-requested-reviewers-for-a-pull-request.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/pulls/:pull_number/requested_reviewers?per_page=30&page=1`

...


### [Request reviewers for a pull request](request-reviewers-for-a-pull-request.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/pulls/:pull_number/requested_reviewers`

This endpoint triggers [notifications](https://help.github.com/articles/about-notifications/). Creat...


### [Remove requested reviewers from a pull request](remove-requested-reviewers-from-a-pull-request.md)

`DELETE` `{{baseUrl}}/repos/:owner/:repo/pulls/:pull_number/requested_reviewers`

...

