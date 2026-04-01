# {hook id}

API endpoints for {hook id}.

## Endpoints


### [Get a repository webhook](get-a-repository-webhook.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/hooks/:hook_id`

...


### [Update a repository webhook](update-a-repository-webhook.md)

`PATCH` `{{baseUrl}}/repos/:owner/:repo/hooks/:hook_id`

...


### [Delete a repository webhook](delete-a-repository-webhook.md)

`DELETE` `{{baseUrl}}/repos/:owner/:repo/hooks/:hook_id`

...


### [Ping a repository webhook](ping-a-repository-webhook.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/hooks/:hook_id/pings`

This will trigger a [ping event](https://developer.github.com/webhooks/#ping-event) to be sent to th...


### [Test the push repository webhook](test-the-push-repository-webhook.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/hooks/:hook_id/tests`

This will trigger the hook with the latest push to the current repository if the hook is subscribed ...

