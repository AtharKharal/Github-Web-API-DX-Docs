# Get an organization webhook



```http
GET {{baseUrl}}/orgs/:org/hooks/:hook_id
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `org` | `string` | `Path` | `Yes` | (Required)  |

| `hook_id` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "200 OK"

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


=== "404 Not Found"

    Resource Not Found

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


