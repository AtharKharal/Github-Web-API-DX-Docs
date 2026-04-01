# List repository webhooks



```http
GET {{baseUrl}}/repos/:owner/:repo/hooks?per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `per_page` | `string` | `Query` | `No` | Results per page (max 100) |

| `page` | `string` | `Query` | `No` | Page number of the results to fetch. |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "200 OK"

    response

    ```json
    [
     {
      "type": "Repository",
      "id": 12345678,
      "name": "web",
      "active": true,
      "events": [
       "push",
       "pull_request"
      ],
      "config": {
       "content_type": "json",
       "insecure_ssl": "0",
       "url": "https://example.com/webhook"
      },
      "updated_at": "2019-06-03T00:57:16Z",
      "created_at": "2019-06-03T00:57:16Z",
      "url": "https://api.github.com/repos/octocat/Hello-World/hooks/12345678",
      "test_url": "https://api.github.com/repos/octocat/Hello-World/hooks/12345678/test",
      "ping_url": "https://api.github.com/repos/octocat/Hello-World/hooks/12345678/pings",
      "last_response": {
       "code": null,
       "status": "unused",
       "message": null
      }
     }
    ]
    ```


=== "404 Not Found"

    Resource Not Found

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


