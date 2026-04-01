# {owner}/{repo}

API endpoints for {owner}/{repo}.

## Endpoints


### [Check if a repository is starred by the authenticated user](check-if-a-repository-is-starred-by-the-authenticated-user.md)

`GET` `{{baseUrl}}/user/starred/:owner/:repo`

...


### [Star a repository for the authenticated user](star-a-repository-for-the-authenticated-user.md)

`PUT` `{{baseUrl}}/user/starred/:owner/:repo`

Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more in...


### [Unstar a repository for the authenticated user](unstar-a-repository-for-the-authenticated-user.md)

`DELETE` `{{baseUrl}}/user/starred/:owner/:repo`

...

