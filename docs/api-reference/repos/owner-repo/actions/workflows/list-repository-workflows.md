# List repository workflows

Lists the workflows in a repository. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint.

```http
GET {{baseUrl}}/repos/:owner/:repo/actions/workflows?per_page=30&page=1
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
     "workflows": [
      {
       "id": 161335,
       "node_id": "MDg6V29ya2Zsb3cxNjEzMzU=",
       "name": "CI",
       "path": ".github/workflows/blank.yml",
       "state": "active",
       "created_at": "2020-01-08T23:48:37.000-08:00",
       "updated_at": "2020-01-08T23:50:21.000-08:00",
       "url": "https://api.github.com/repos/octo-org/octo-repo/actions/workflows/161335",
       "html_url": "https://github.com/octo-org/octo-repo/blob/master/.github/workflows/161335",
       "badge_url": "https://github.com/octo-org/octo-repo/workflows/CI/badge.svg"
      },
      {
       "id": 269289,
       "node_id": "MDE4OldvcmtmbG93IFNlY29uZGFyeTI2OTI4OQ==",
       "name": "Linter",
       "path": ".github/workflows/linter.yml",
       "state": "active",
       "created_at": "2020-01-08T23:48:37.000-08:00",
       "updated_at": "2020-01-08T23:50:21.000-08:00",
       "url": "https://api.github.com/repos/octo-org/octo-repo/actions/workflows/269289",
       "html_url": "https://github.com/octo-org/octo-repo/blob/master/.github/workflows/269289",
       "badge_url": "https://github.com/octo-org/octo-repo/workflows/Linter/badge.svg"
      }
     ]
    }
    ```


