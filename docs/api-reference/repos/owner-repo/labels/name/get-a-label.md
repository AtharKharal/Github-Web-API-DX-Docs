# Get a label



```http
GET {{baseUrl}}/repos/:owner/:repo/labels/:name
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `name` | `string` | `Path` | `Yes` | (Required) name parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "404 Not Found"

    Resource Not Found

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "200 OK"

    response

    ```json
    {
     "id": 208045946,
     "node_id": "MDU6TGFiZWwyMDgwNDU5NDY=",
     "url": "https://api.github.com/repos/octocat/Hello-World/labels/bug",
     "name": "bug",
     "description": "Something isn't working",
     "color": "f29513",
     "default": true
    }
    ```


