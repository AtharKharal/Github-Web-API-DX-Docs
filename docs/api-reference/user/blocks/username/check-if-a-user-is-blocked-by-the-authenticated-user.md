# Check if a user is blocked by the authenticated user

If the user is blocked:

If the user is not blocked:

```http
GET {{baseUrl}}/user/blocks/:username
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `username` | `string` | `Path` | `Yes` | (Required)  |



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


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


=== "404 Not Found"

    If the user is not blocked:

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "401 Unauthorized"

    Requires Authentication

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "204 No Content"

    If the user is blocked:

    ```json
    
    ```


