# Get a self-hosted runner for a repository

Gets a specific self-hosted runner. You must authenticate using an access token with the `repo` scope to use this endpoint.

```http
GET {{baseUrl}}/repos/:owner/:repo/actions/runners/:runner_id
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `runner_id` | `string` | `Path` | `Yes` | (Required) runner_id parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "200 OK"

    response

    ```json
    {
     "id": 23,
     "name": "MBP",
     "os": "macos",
     "status": "online"
    }
    ```


