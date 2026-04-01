# Delete an organization migration archive

Deletes a previous migration archive. Migration archives are automatically deleted after seven days.

```http
DELETE {{baseUrl}}/orgs/:org/migrations/:migration_id/archive
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


=== "404 Not Found"

    Resource Not Found

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "204 No Content"

    Empty response

    ```json
    
    ```


