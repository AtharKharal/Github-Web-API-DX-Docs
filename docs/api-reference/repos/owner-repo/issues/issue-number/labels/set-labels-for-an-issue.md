# Set labels for an issue

Removes any previous labels and sets the new labels for an issue.

```http
PUT {{baseUrl}}/repos/:owner/:repo/issues/:issue_number/labels
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `issue_number` | `string` | `Path` | `Yes` | (Required) issue_number parameter |



## Request Body

=== "JSON"

    ```json
    {
        "labels": [
            "<string>",
            "<string>"
        ]
    }
    ```


## Responses


=== "410 Gone"

    Gone

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


=== "200 OK"

    response

    ```json
    [
     {
      "id": 208045946,
      "node_id": "MDU6TGFiZWwyMDgwNDU5NDY=",
      "url": "https://api.github.com/repos/octocat/Hello-World/labels/bug",
      "name": "bug",
      "description": "Something isn't working",
      "color": "f29513",
      "default": true
     },
     {
      "id": 208045947,
      "node_id": "MDU6TGFiZWwyMDgwNDU5NDc=",
      "url": "https://api.github.com/repos/octocat/Hello-World/labels/enhancement",
      "name": "enhancement",
      "description": "New feature or request",
      "color": "a2eeef",
      "default": false
     }
    ]
    ```


