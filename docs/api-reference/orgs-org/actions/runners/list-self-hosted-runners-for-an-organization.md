# List self-hosted runners for an organization

**Warning:** The self-hosted runners API for organizations is currently in public beta and subject to change.

Lists all self-hosted runners for an organization. You must authenticate using an access token with the `admin:org` scope to use this endpoint.

```http
GET {{baseUrl}}/orgs/:org/actions/runners?per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `org` | `string` | `Path` | `Yes` | (Required)  |

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


