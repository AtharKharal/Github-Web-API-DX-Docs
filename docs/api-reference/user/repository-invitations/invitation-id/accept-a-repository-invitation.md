# Accept a repository invitation



```http
PATCH {{baseUrl}}/user/repository_invitations/:invitation_id
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `invitation_id` | `string` | `Path` | `Yes` | (Required) invitation_id parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "403 Forbidden"

    Forbidden

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


=== "404 Not Found"

    Resource Not Found

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


=== "409 Conflict"

    Conflict

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


