# Convert an organization member to outside collaborator

When an organization member is converted to an outside collaborator, they'll only have access to the repositories that their current team membership allows. The user will no longer be a member of the organization. For more information, see "[Converting an organization member to an outside collaborator](https://help.github.com/articles/converting-an-organization-member-to-an-outside-collaborator/)".

```http
PUT {{baseUrl}}/orgs/:org/outside_collaborators/:username
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


=== "202 Accepted"

    User is getting converted asynchronously

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


=== "204 No Content"

    User was converted

    ```json
    
    ```


=== "403 Forbidden"

    response

    ```json
    {
     "message": "Cannot convert the last owner to an outside collaborator",
     "documentation_url": "https://developer.github.com/v3/orgs/outside_collaborators/#convert-member-to-outside-collaborator"
    }
    ```


