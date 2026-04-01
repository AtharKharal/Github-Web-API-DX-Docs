# Check if a user can be assigned

Checks if a user has permission to be assigned to an issue in this repository.

If the `assignee` can be assigned to issues in the repository, a `204` header with no content is returned.

Otherwise a `404` status code is returned.

```http
GET {{baseUrl}}/repos/:owner/:repo/assignees/:assignee
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `assignee` | `string` | `Path` | `Yes` | (Required) assignee parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "204 No Content"

    If the `assignee` can be assigned to issues in the repository, a `204` header with no content is returned.

    ```json
    
    ```


=== "404 Not Found"

    Otherwise a `404` status code is returned.

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


