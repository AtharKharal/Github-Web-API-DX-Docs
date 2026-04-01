# Check if a user is blocked by an organization



```http
GET {{baseUrl}}/orgs/:org/blocks/:username
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `org` | `string` | `Path` | `Yes` | (Required)  |

| `username` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "404 Not Found"

    If the user is not blocked:

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


