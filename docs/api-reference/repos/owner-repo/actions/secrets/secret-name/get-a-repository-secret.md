# Get a repository secret

Gets a single repository secret without revealing its encrypted value. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `secrets` repository permission to use this endpoint.

```http
GET {{baseUrl}}/repos/:owner/:repo/actions/secrets/:secret_name
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `secret_name` | `string` | `Path` | `Yes` | (Required) secret_name parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "200 OK"

    response

    ```json
    {
     "name": "GH_TOKEN",
     "created_at": "2019-08-10T14:59:22Z",
     "updated_at": "2020-01-10T14:59:22Z"
    }
    ```


