# Get a self-hosted runner for an organization

**Warning:** The self-hosted runners API for organizations is currently in public beta and subject to change.

Gets a specific self-hosted runner for an organization. You must authenticate using an access token with the `admin:org` scope to use this endpoint.

```http
GET {{baseUrl}}/orgs/:org/actions/runners/:runner_id
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `org` | `string` | `Path` | `Yes` | (Required)  |

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


