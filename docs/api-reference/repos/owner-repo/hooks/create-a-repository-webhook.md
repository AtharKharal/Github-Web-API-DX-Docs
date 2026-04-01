# Create a repository webhook

Repositories can have multiple webhooks installed. Each webhook should have a unique `config`. Multiple webhooks can
share the same `config` as long as those webhooks do not have any `events` that overlap.

```http
POST {{baseUrl}}/repos/:owner/:repo/hooks
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
        "config": {
            "url": "<string>",
            "content_type": "<string>",
            "secret": "<string>",
            "insecure_ssl": "<string>",
            "token": "<string>",
            "digest": "<string>"
        },
        "name": "<string>",
        "events": [
            "push"
        ],
        "active": true
    }
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


=== "403 Forbidden"

    Forbidden

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


=== "201 Created"

    response

    ```json
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
    ```


