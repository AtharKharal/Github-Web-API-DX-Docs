# List self-hosted runners for a repository

Lists all self-hosted runners for a repository. You must authenticate using an access token with the `repo` scope to use this endpoint.

```http
GET {{baseUrl}}/repos/:owner/:repo/actions/runners?per_page=30&page=1
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
     "runners": [
      {
       "id": 23,
       "name": "MBP",
       "os": "macos",
       "status": "online"
      },
      {
       "id": 24,
       "name": "iMac",
       "os": "macos",
       "status": "offline"
      }
     ]
    }
    ```


