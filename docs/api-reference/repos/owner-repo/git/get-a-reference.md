# Get a reference

Returns a single reference from your Git database. The `:ref` in the URL must be formatted as `heads/<branch name>` for branches and `tags/<tag name>` for tags. If the `:ref` doesn't match an existing ref, a `404` is returned.

**Note:** You need to explicitly [request a pull request](https://developer.github.com/v3/pulls/#get-a-pull-request) to trigger a test merge commit, which checks the mergeability of pull requests. For more information, see "[Checking mergeability of pull requests](https://developer.github.com/v3/git/#checking-mergeability-of-pull-requests)".

```http
GET {{baseUrl}}/repos/:owner/:repo/git/ref/:ref
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `ref` | `string` | `Path` | `Yes` | (Required) ref+ parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "404 Not Found"

    Resource Not Found

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "200 OK"

    response

    ```json
    {
     "ref": "refs/heads/featureA",
     "node_id": "MDM6UmVmcmVmcy9oZWFkcy9mZWF0dXJlQQ==",
     "url": "https://api.github.com/repos/octocat/Hello-World/git/refs/heads/featureA",
     "object": {
      "type": "commit",
      "sha": "aa218f56b14c9653891f9e74264a383fa43fefbd",
      "url": "https://api.github.com/repos/octocat/Hello-World/git/commits/aa218f56b14c9653891f9e74264a383fa43fefbd"
     }
    }
    ```


