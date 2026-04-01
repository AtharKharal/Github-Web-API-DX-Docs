# Get a workflow

Gets a specific workflow. You can also replace `:workflow_id` with `:workflow_file_name`. For example, you could use `main.yml`. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint.

```http
GET {{baseUrl}}/repos/:owner/:repo/actions/workflows/:workflow_id
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `workflow_id` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "200 OK"

    response

    ```json
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
    }
    ```


