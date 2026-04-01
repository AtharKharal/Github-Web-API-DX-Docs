# merge

API endpoints for merge.

## Endpoints


### [Check if a pull request has been merged](check-if-a-pull-request-has-been-merged.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/pulls/:pull_number/merge`

...


### [Merge a pull request](merge-a-pull-request.md)

`PUT` `{{baseUrl}}/repos/:owner/:repo/pulls/:pull_number/merge`

This endpoint triggers [notifications](https://help.github.com/articles/about-notifications/). Creat...

