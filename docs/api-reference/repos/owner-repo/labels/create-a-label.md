# Create a label



```http
POST {{baseUrl}}/repos/:owner/:repo/labels
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
        "name": "<string>",
        "color": "<string>",
        "description": "<string>"
    }
    ```


## Responses


=== "201 Created"

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


=== "404 Not Found"

    Resource Not Found

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "422 Unprocessable Entity (WebDAV) (RFC 4918)"

    Validation Failed

    ```json
    {
     "message": "culpa mollit",
     "documentation_url": "ipsum ut",
     "errors": [
      {
       "code": "consequat enim et velit",
       "resource": "anim ullamco",
       "field": "voluptate officia amet",
       "message": "exercitation sed dolore est",
       "index": 18359415,
       "value": "ullamco ut velit nulla eiusmod"
      },
      {
       "code": "occaecat eiusmod Duis",
       "resource": "esse ad Excepteur mollit",
       "field": "minim ipsum nisi exercitation non",
       "message": "proident reprehenderit",
       "index": -23326731,
       "value": "adipisicing cupidatat culpa in"
      }
     ]
    }
    ```


