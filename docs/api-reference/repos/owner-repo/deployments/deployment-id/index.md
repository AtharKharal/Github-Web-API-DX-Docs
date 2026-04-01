# {deployment id}

API endpoints for {deployment id}.

## Endpoints


### [statuses](statuses/index.md)

`` ``




### [Get a deployment](get-a-deployment.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/deployments/:deployment_id`

...


### [Delete a deployment](delete-a-deployment.md)

`DELETE` `{{baseUrl}}/repos/:owner/:repo/deployments/:deployment_id`

To ensure there can always be an active deployment, you can only delete an _inactive_ deployment. An...

