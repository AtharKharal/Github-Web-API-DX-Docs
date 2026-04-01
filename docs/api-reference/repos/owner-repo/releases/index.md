# releases

API endpoints for releases.

## Endpoints


### [assets/{asset id}](assets-asset-id/index.md)

`` ``




### [{release id}](release-id/index.md)

`` ``




### [List releases](list-releases.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/releases?per_page=30&page=1`

This returns a list of releases, which does not include regular Git tags that have not been associat...


### [Create a release](create-a-release.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/releases`

Users with push access to the repository can create a release.

This endpoint triggers [notification...


### [Get the latest release](get-the-latest-release.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/releases/latest`

View the latest published full release for the repository.

The latest release is the most recent no...


### [Get a release by tag name](get-a-release-by-tag-name.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/releases/tags/:tag`

Get a published release with the specified tag....

