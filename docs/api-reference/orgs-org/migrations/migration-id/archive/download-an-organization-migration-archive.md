# Download an organization migration archive

Fetches the URL to a migration archive.

```http
GET {{baseUrl}}/orgs/:org/migrations/:migration_id/archive
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `org` | `string` | `Path` | `Yes` | (Required)  |

| `migration_id` | `string` | `Path` | `Yes` | (Required) migration_id parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "302 Found"

    response

    ```json
    
    ```


=== "404 Not Found"

    Resource Not Found

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


