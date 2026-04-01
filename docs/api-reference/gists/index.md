# gists

API endpoints for gists.

## Endpoints


### [{gist id}](gist-id/index.md)

`` ``




### [List gists for the authenticated user](list-gists-for-the-authenticated-user.md)

`GET` `{{baseUrl}}/gists?since=<string>&per_page=30&page=1`

Lists the authenticated user's gists or if called anonymously, this endpoint returns all public gist...


### [Create a gist](create-a-gist.md)

`POST` `{{baseUrl}}/gists`

Allows you to add a new gist with one or more files.

**Note:** Don't name your files "gistfile" wit...


### [List public gists](list-public-gists.md)

`GET` `{{baseUrl}}/gists/public?since=<string>&per_page=30&page=1`

List public gists sorted by most recently updated to least recently updated.

Note: With [pagination...


### [List starred gists](list-starred-gists.md)

`GET` `{{baseUrl}}/gists/starred?since=<string>&per_page=30&page=1`

List the authenticated user's starred gists:...

