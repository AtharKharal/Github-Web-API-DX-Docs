# Get an artifact

Gets a specific artifact for a workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint.

```http
GET {{baseUrl}}/repos/:owner/:repo/actions/artifacts/:artifact_id
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `artifact_id` | `string` | `Path` | `Yes` | (Required) artifact_id parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "200 OK"

    response

    ```json
    {
     "id": 11,
     "node_id": "MDg6QXJ0aWZhY3QxMQ==",
     "name": "Rails",
     "size_in_bytes": 556,
     "url": "https://api.github.com/repos/octo-org/octo-docs/actions/artifacts/11",
     "archive_download_url": "https://api.github.com/repos/octo-org/octo-docs/actions/artifacts/11/zip",
     "expired": false,
     "created_at": "2020-01-10T14:59:22Z",
     "expires_at": "2020-01-21T14:59:22Z",
     "updated_at": "2020-01-21T14:59:22Z"
    }
    ```


