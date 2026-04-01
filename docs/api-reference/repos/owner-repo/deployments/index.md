# deployments

API endpoints for deployments.

## Endpoints


### [{deployment id}](deployment-id/index.md)

`` ``




### [List deployments](list-deployments.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/deployments?sha=none&ref=none&task=none&environment=none&per_page=30&page=1`

Simple filtering of deployments is available via query parameters:...


### [Create a deployment](create-a-deployment.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/deployments`

Deployments offer a few configurable parameters with certain defaults.

The `ref` parameter can be a...

