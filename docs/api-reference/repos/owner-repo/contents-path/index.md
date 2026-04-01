# contents/{path}

API endpoints for contents/{path}.

## Endpoints


### [Get repository content](get-repository-content.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/contents/:path?ref=<string>`

Gets the contents of a file or directory in a repository. Specify the file path or directory in `:pa...


### [Create or update file contents](create-or-update-file-contents.md)

`PUT` `{{baseUrl}}/repos/:owner/:repo/contents/:path`

Creates a new file or replaces an existing file in a repository....


### [Delete a file](delete-a-file.md)

`DELETE` `{{baseUrl}}/repos/:owner/:repo/contents/:path`

Deletes a file in a repository.

You can provide an additional `committer` parameter, which is an ob...

