# Download workflow run logs

Gets a redirect URL to download an archive of log files for a workflow run. This link expires after 1 minute. Look for
`Location:` in the response header to find the URL for the download. Anyone with read access to the repository can use
this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have
the `actions:read` permission to use this endpoint.

```http
GET {{baseUrl}}/repos/:owner/:repo/actions/runs/:run_id/logs
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `run_id` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "302 Found"

    response

    ```json
    
    ```


