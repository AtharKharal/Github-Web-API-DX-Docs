# List organization secrets

Lists all secrets available in an organization without revealing their encrypted values. You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint.

```http
GET {{baseUrl}}/orgs/:org/actions/secrets?per_page=30&page=1
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
     "total_count": 3,
     "secrets": [
      {
       "name": "GIST_ID",
       "created_at": "2019-08-10T14:59:22Z",
       "updated_at": "2020-01-10T14:59:22Z",
       "visibility": "private"
      },
      {
       "name": "DEPLOY_TOKEN",
       "created_at": "2019-08-10T14:59:22Z",
       "updated_at": "2020-01-10T14:59:22Z",
       "visibility": "all"
      },
      {
       "name": "GH_TOKEN",
       "created_at": "2019-08-10T14:59:22Z",
       "updated_at": "2020-01-10T14:59:22Z",
       "visibility": "selected",
       "selected_repositories_url": "https://api.github.com/orgs/octo-org/actions/secrets/SUPER_SECRET/repositories"
      }
     ]
    }
    ```


