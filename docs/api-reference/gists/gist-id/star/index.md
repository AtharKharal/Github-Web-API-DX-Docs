# star

API endpoints for star.

## Endpoints


### [Check if a gist is starred](check-if-a-gist-is-starred.md)

`GET` `{{baseUrl}}/gists/:gist_id/star`

...


### [Star a gist](star-a-gist.md)

`PUT` `{{baseUrl}}/gists/:gist_id/star`

Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more in...


### [Unstar a gist](unstar-a-gist.md)

`DELETE` `{{baseUrl}}/gists/:gist_id/star`

...

