# statuses

API endpoints for statuses.

## Endpoints


### [List deployment statuses](list-deployment-statuses.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/deployments/:deployment_id/statuses?per_page=30&page=1`

Users with pull access can view deployment statuses for a deployment:...


### [Create a deployment status](create-a-deployment-status.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/deployments/:deployment_id/statuses`

Users with `push` access can create deployment statuses for a given deployment.

GitHub Apps require...


### [Get a deployment status](get-a-deployment-status.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/deployments/:deployment_id/statuses/:status_id`

Users with pull access can view a deployment status for a deployment:...

