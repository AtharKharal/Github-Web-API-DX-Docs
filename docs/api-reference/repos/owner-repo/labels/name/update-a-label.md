# Update a label



```http
PATCH {{baseUrl}}/repos/:owner/:repo/labels/:name
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
    {
        "new_name": "<string>",
        "color": "<string>",
        "description": "<string>"
    }
    ```


## Responses


=== "200 OK"

    response

    ```json
    {
     "id": 208045946,
     "node_id": "MDU6TGFiZWwyMDgwNDU5NDY=",
     "url": "https://api.github.com/repos/octocat/Hello-World/labels/bug%20:bug:",
     "name": "bug :bug:",
     "description": "Small bug fix required",
     "color": "b01f26",
     "default": true
    }
    ```


