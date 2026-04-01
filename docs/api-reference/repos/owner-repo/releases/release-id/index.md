# {release id}

API endpoints for {release id}.

## Endpoints


### [assets](assets/index.md)

`` ``




### [Get a release](get-a-release.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/releases/:release_id`

**Note:** This returns an `upload_url` key corresponding to the endpoint for uploading release asset...


### [Update a release](update-a-release.md)

`PATCH` `{{baseUrl}}/repos/:owner/:repo/releases/:release_id`

Users with push access to the repository can edit a release....


### [Delete a release](delete-a-release.md)

`DELETE` `{{baseUrl}}/repos/:owner/:repo/releases/:release_id`

Users with push access to the repository can delete a release....

