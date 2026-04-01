# Download an artifact

Gets a redirect URL to download an archive for a repository. This URL expires after 1 minute. Look for `Location:` in
the response header to find the URL for the download. The `:archive_format` must be `zip`. Anyone with read access to
the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope.
GitHub Apps must have the `actions:read` permission to use this endpoint.

```http
GET {{baseUrl}}/repos/:owner/:repo/actions/artifacts/:artifact_id/:archive_format
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `artifact_id` | `string` | `Path` | `Yes` | (Required) artifact_id parameter |

| `archive_format` | `string` | `Path` | `Yes` | (Required) archive_format parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "302 Found"

    response

    ```json
    
    ```


