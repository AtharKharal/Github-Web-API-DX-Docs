# Create an organization webhook

Here's how you can create a hook that posts payloads in JSON format:

```http
POST {{baseUrl}}/orgs/:org/hooks
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `org` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    {
        "name": "<string>",
        "config": {
            "url": "<string>",
            "content_type": "<string>",
            "secret": "<string>",
            "insecure_ssl": "<string>",
            "username": "<string>",
            "password": "<string>"
        },
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
     "id": 1,
     "url": "https://api.github.com/orgs/octocat/hooks/1",
     "ping_url": "https://api.github.com/orgs/octocat/hooks/1/pings",
     "name": "web",
     "events": [
      "push",
      "pull_request"
     ],
     "active": true,
     "config": {
      "url": "http://example.com",
      "content_type": "json"
     },
     "updated_at": "2011-09-06T20:39:23Z",
     "created_at": "2011-09-06T17:26:27Z",
     "type": "Organization"
    }
    ```


