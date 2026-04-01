# List artifacts for a repository

Lists all artifacts for a repository. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint.

```http
GET {{baseUrl}}/repos/:owner/:repo/actions/artifacts?per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `per_page` | `string` | `Query` | `No` | Results per page (max 100) |

| `page` | `string` | `Query` | `No` | Page number of the results to fetch. |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "200 OK"

    response

    ```json
    {
     "total_count": 2,
     "artifacts": [
      {
       "id": 11,
       "node_id": "MDg6QXJ0aWZhY3QxMQ==",
       "name": "Rails",
       "size_in_bytes": 556,
       "url": "https://api.github.com/repos/octo-org/octo-docs/actions/artifacts/11",
       "archive_download_url": "https://api.github.com/repos/octo-org/octo-docs/actions/artifacts/11/zip",
       "expired": false,
       "created_at": "2020-01-10T14:59:22Z",
       "expires_at": "2020-03-21T14:59:22Z",
       "updated_at": "2020-02-21T14:59:22Z"
      },
      {
       "id": 13,
       "node_id": "MDg6QXJ0aWZhY3QxMw==",
       "name": "",
       "size_in_bytes": 453,
       "url": "https://api.github.com/repos/octo-org/octo-docs/actions/artifacts/13",
       "archive_download_url": "https://api.github.com/repos/octo-org/octo-docs/actions/artifacts/13/zip",
       "expired": false,
       "created_at": "2020-01-10T14:59:22Z",
       "expires_at": "2020-03-21T14:59:22Z",
       "updated_at": "2020-02-21T14:59:22Z"
      }
     ]
    }
    ```


