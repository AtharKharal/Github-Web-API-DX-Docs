# {key id}

API endpoints for {key id}.

## Endpoints


### [Get a deploy key](get-a-deploy-key.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/keys/:key_id`

...


### [Delete a deploy key](delete-a-deploy-key.md)

`DELETE` `{{baseUrl}}/repos/:owner/:repo/keys/:key_id`

Deploy keys are immutable. If you need to update a key, remove the key and create a new one instead....

