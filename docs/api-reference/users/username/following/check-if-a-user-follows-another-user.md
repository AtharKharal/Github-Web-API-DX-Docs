# Check if a user follows another user



```http
GET {{baseUrl}}/users/:username/following/:target_user
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `username` | `string` | `Path` | `Yes` | (Required)  |

| `target_user` | `string` | `Path` | `Yes` | (Required) target_user parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "204 No Content"

    Response if the user follows the target user

    ```json
    
    ```


=== "404 Not Found"

    Response if the user does not follow the target user

    ```json
    
    ```


