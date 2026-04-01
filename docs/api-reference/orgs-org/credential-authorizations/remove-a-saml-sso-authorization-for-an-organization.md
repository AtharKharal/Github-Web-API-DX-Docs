# Remove a SAML SSO authorization for an organization

Listing and deleting credential authorizations is available to organizations with GitHub Enterprise Cloud. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products).

An authenticated organization owner with the `admin:org` scope can remove a credential authorization for an organization that uses SAML SSO. Once you remove someone's credential authorization, they will need to create a new personal access token or SSH key and authorize it for the organization they want to access.

```http
DELETE {{baseUrl}}/orgs/:org/credential-authorizations/:credential_id
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `org` | `string` | `Path` | `Yes` | (Required)  |

| `credential_id` | `string` | `Path` | `Yes` | (Required) credential_id parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


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


