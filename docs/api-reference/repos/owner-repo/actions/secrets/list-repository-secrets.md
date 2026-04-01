# List repository secrets

Lists all secrets available in a repository without revealing their encrypted values. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `secrets` repository permission to use this endpoint.

```http
GET {{baseUrl}}/repos/:owner/:repo/actions/secrets?per_page=30&page=1
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
     "secrets": [
      {
       "name": "GH_TOKEN",
       "created_at": "2019-08-10T14:59:22Z",
       "updated_at": "2020-01-10T14:59:22Z"
      },
      {
       "name": "GIST_ID",
       "created_at": "2020-01-10T10:59:22Z",
       "updated_at": "2020-01-11T11:59:22Z"
      }
     ]
    }
    ```


