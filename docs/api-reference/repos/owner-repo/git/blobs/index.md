# blobs

API endpoints for blobs.

## Endpoints


### [Create a blob](create-a-blob.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/git/blobs`

...


### [Get a blob](get-a-blob.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/git/blobs/:file_sha`

The `content` in the response will always be Base64 encoded.

_Note_: This API supports blobs up to ...

