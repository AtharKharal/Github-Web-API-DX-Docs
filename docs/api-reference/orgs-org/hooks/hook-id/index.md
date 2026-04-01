# {hook id}

API endpoints for {hook id}.

## Endpoints


### [Get an organization webhook](get-an-organization-webhook.md)

`GET` `{{baseUrl}}/orgs/:org/hooks/:hook_id`

...


### [Update an organization webhook](update-an-organization-webhook.md)

`PATCH` `{{baseUrl}}/orgs/:org/hooks/:hook_id`

...


### [Delete an organization webhook](delete-an-organization-webhook.md)

`DELETE` `{{baseUrl}}/orgs/:org/hooks/:hook_id`

...


### [Ping an organization webhook](ping-an-organization-webhook.md)

`POST` `{{baseUrl}}/orgs/:org/hooks/:hook_id/pings`

This will trigger a [ping event](https://developer.github.com/webhooks/#ping-event) to be sent to th...

