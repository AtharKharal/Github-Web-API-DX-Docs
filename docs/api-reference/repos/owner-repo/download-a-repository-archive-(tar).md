# Download a repository archive (tar)

Gets a redirect URL to download a tar archive for a repository. If you omit `:ref`, the repository’s default branch (usually
`master`) will be used. Please make sure your HTTP framework is configured to follow redirects or you will need to use
the `Location` header to make a second `GET` request.
**Note**: For private repositories, these links are temporary and expire after five minutes.

```http
GET {{baseUrl}}/repos/:owner/:repo/tarball/:ref
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `ref` | `string` | `Path` | `Yes` | (Required) ref parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "302 Found"

    response

    ```json
    
    ```


