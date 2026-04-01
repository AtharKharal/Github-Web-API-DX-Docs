# assets

API endpoints for assets.

## Endpoints


### [List release assets](list-release-assets.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/releases/:release_id/assets?per_page=30&page=1`

...


### [Upload a release asset](upload-a-release-asset.md)

`POST` `{{origin}}/repos/:owner/:repo/releases/:release_id/assets?name=<string>&label=<string>`

This endpoint makes use of [a Hypermedia relation](https://developer.github.com/v3/#hypermedia) to d...

