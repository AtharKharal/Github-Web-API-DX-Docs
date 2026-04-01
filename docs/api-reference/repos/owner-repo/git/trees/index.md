# trees

API endpoints for trees.

## Endpoints


### [Create a tree](create-a-tree.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/git/trees`

The tree creation API accepts nested entries. If you specify both a tree and a nested path modifying...


### [Get a tree](get-a-tree.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/git/trees/:tree_sha?recursive=<string>`

Returns a single tree using the SHA1 value for that tree.

If `truncated` is `true` in the response ...

