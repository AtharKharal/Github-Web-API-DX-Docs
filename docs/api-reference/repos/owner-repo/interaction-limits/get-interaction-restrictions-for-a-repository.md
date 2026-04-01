# Get interaction restrictions for a repository

Shows which group of GitHub users can interact with this repository and when the restriction expires. If there are no restrictions, you will see an empty response.

```http
GET {{baseUrl}}/repos/:owner/:repo/interaction-limits
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    
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


