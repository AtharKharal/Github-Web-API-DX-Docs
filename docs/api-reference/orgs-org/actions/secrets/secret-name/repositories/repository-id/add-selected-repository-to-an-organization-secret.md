# Add selected repository to an organization secret

Adds a repository to an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://developer.github.com/v3/actions/secrets/#create-or-update-an-organization-secret). You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint.

```http
PUT {{baseUrl}}/orgs/:org/actions/secrets/:secret_name/repositories/:repository_id
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `org` | `string` | `Path` | `Yes` | (Required)  |

| `secret_name` | `string` | `Path` | `Yes` | (Required) secret_name parameter |

| `repository_id` | `string` | `Path` | `Yes` | (Required) repository_id parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "409 Conflict"

    Response when visibility type is not set to selected

    ```json
    
    ```


=== "204 No Content"

    Response when repository was added to the selected list

    ```json
    
    ```


