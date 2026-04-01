# Set selected repositories for an organization secret

Replaces all repositories for an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://developer.github.com/v3/actions/secrets/#create-or-update-an-organization-secret). You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint.

```http
PUT {{baseUrl}}/orgs/:org/actions/secrets/:secret_name/repositories
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `org` | `string` | `Path` | `Yes` | (Required)  |

| `secret_name` | `string` | `Path` | `Yes` | (Required) secret_name parameter |



## Request Body

=== "JSON"

    ```json
    {
        "selected_repository_ids": [
            "<integer>",
            "<integer>"
        ]
    }
    ```


## Responses


=== "204 No Content"

    Empty response

    ```json
    
    ```


