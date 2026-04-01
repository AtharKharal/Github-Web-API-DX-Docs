# Check organization membership for a user

Check if a user is, publicly or privately, a member of the organization.

```http
GET {{baseUrl}}/orgs/:org/members/:username
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

    Response if requester is an organization member and user is not a member

    ```json
    
    ```


=== "204 No Content"

    Response if requester is an organization member and user is a member

    ```json
    
    ```


=== "302 Found"

    Response if requester is not an organization member

    ```json
    
    ```


