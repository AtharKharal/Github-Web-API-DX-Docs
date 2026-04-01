# git

API endpoints for git.

## Endpoints


### [blobs](blobs/index.md)

`` ``




### [commits](commits/index.md)

`` ``




### [refs](refs/index.md)

`` ``




### [tags](tags/index.md)

`` ``




### [trees](trees/index.md)

`` ``




### [List matching references](list-matching-references.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/git/matching-refs/:ref?per_page=30&page=1`

Returns an array of references from your Git database that match the supplied name. The `:ref` in th...


### [Get a reference](get-a-reference.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/git/ref/:ref`

Returns a single reference from your Git database. The `:ref` in the URL must be formatted as `heads...

