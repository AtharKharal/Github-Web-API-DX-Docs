# Delete a project column



```http
DELETE {{baseUrl}}/projects/columns/:column_id
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `column_id` | `string` | `Path` | `Yes` | (Required) column_id parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "401 Unauthorized"

    Requires Authentication

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


=== "204 No Content"

    Empty response

    ```json
    
    ```


=== "403 Forbidden"

    Forbidden

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


