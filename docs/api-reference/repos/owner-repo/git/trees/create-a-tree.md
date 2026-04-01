# Create a tree

The tree creation API accepts nested entries. If you specify both a tree and a nested path modifying that tree, this endpoint will overwrite the contents of the tree with the new path contents, and create a new tree structure.

If you use this endpoint to add, delete, or modify the file contents in a tree, you will need to commit the tree and then update a branch to point to the commit. For more information see "[Create a commit](https://developer.github.com/v3/git/commits/#create-a-commit)" and "[Update a reference](https://developer.github.com/v3/git/refs/#update-a-reference)."

```http
POST {{baseUrl}}/repos/:owner/:repo/git/trees
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    {
        "tree": [
            {
                "path": "<string>",
                "mode": "<string>",
                "type": "<string>",
                "sha": "<string>",
                "content": "<string>"
            },
            {
                "path": "<string>",
                "mode": "<string>",
                "type": "<string>",
                "sha": "<string>",
                "content": "<string>"
            }
        ],
        "base_tree": "<string>"
    }
    ```


## Responses


=== "201 Created"

    response

    ```json
    {
     "sha": "cd8274d15fa3ae2ab983129fb037999f264ba9a7",
     "url": "https://api.github.com/repos/octocat/Hello-World/trees/cd8274d15fa3ae2ab983129fb037999f264ba9a7",
     "tree": [
      {
       "path": "file.rb",
       "mode": "100644",
       "type": "blob",
       "size": 132,
       "sha": "7c258a9869f33c1e1e1f74fbb32f07c86cb5a75b",
       "url": "https://api.github.com/repos/octocat/Hello-World/git/blobs/7c258a9869f33c1e1e1f74fbb32f07c86cb5a75b"
      }
     ],
     "truncated": true
    }
    ```


=== "404 Not Found"

    Resource Not Found

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "422 Unprocessable Entity (WebDAV) (RFC 4918)"

    Validation Failed

    ```json
    {
     "message": "culpa mollit",
     "documentation_url": "ipsum ut",
     "errors": [
      {
       "code": "consequat enim et velit",
       "resource": "anim ullamco",
       "field": "voluptate officia amet",
       "message": "exercitation sed dolore est",
       "index": 18359415,
       "value": "ullamco ut velit nulla eiusmod"
      },
      {
       "code": "occaecat eiusmod Duis",
       "resource": "esse ad Excepteur mollit",
       "field": "minim ipsum nisi exercitation non",
       "message": "proident reprehenderit",
       "index": -23326731,
       "value": "adipisicing cupidatat culpa in"
      }
     ]
    }
    ```


=== "403 Forbidden"

    Forbidden

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


