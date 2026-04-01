# assets/{asset id}

API endpoints for assets/{asset id}.

## Endpoints


### [Get a release asset](get-a-release-asset.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/releases/assets/:asset_id`

To download the asset's binary content, set the `Accept` header of the request to [`application/octe...


### [Update a release asset](update-a-release-asset.md)

`PATCH` `{{baseUrl}}/repos/:owner/:repo/releases/assets/:asset_id`

Users with push access to the repository can edit a release asset....


### [Delete a release asset](delete-a-release-asset.md)

`DELETE` `{{baseUrl}}/repos/:owner/:repo/releases/assets/:asset_id`

...

