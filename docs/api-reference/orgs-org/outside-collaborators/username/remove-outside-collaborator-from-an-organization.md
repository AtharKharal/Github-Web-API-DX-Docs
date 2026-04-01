# Remove outside collaborator from an organization

Removing a user from this list will remove them from all the organization's repositories.

```http
DELETE {{baseUrl}}/orgs/:org/outside_collaborators/:username
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


=== "204 No Content"

    Empty response

    ```json
    
    ```


=== "422 Unprocessable Entity (WebDAV) (RFC 4918)"

    Response if user is a member of the organization

    ```json
    {
     "message": "You cannot specify an organization member to remove as an outside collaborator.",
     "documentation_url": "https://developer.github.com/v3/orgs/outside_collaborators/#remove-outside-collaborator"
    }
    ```


