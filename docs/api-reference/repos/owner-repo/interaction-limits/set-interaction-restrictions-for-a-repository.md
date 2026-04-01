# Set interaction restrictions for a repository

Temporarily restricts interactions to certain GitHub users within the given repository. You must have owner or admin access to set restrictions.

```http
PUT {{baseUrl}}/repos/:owner/:repo/interaction-limits
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    {
        "limit": "<string>"
    }
    ```


## Responses


=== "200 OK"

    response

    ```json
    {
     "limit": "collaborators_only",
     "origin": "repository",
     "expires_at": "2018-08-17T04:18:39Z"
    }
    ```


