# Get a GitHub Pages site



```http
GET {{baseUrl}}/repos/:owner/:repo/pages
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
     "url": "https://api.github.com/repos/github/developer.github.com/pages",
     "status": "built",
     "cname": "developer.github.com",
     "custom_404": false,
     "html_url": "https://developer.github.com",
     "source": {
      "branch": "master",
      "path": "/"
     }
    }
    ```


