# Check public organization membership for a user



```http
GET {{baseUrl}}/orgs/:org/public_members/:username
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

    Response if user is not a public member

    ```json
    
    ```


=== "204 No Content"

    Response if user is a public member

    ```json
    
    ```


