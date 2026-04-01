# subscription

API endpoints for subscription.

## Endpoints


### [Get a repository subscription](get-a-repository-subscription.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/subscription`

...


### [Set a repository subscription](set-a-repository-subscription.md)

`PUT` `{{baseUrl}}/repos/:owner/:repo/subscription`

If you would like to watch a repository, set `subscribed` to `true`. If you would like to ignore not...


### [Delete a repository subscription](delete-a-repository-subscription.md)

`DELETE` `{{baseUrl}}/repos/:owner/:repo/subscription`

This endpoint should only be used to stop watching a repository. To control whether or not you wish ...

