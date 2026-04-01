# Get a gist comment



```http
GET {{baseUrl}}/gists/:gist_id/comments/:comment_id
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `gist_id` | `string` | `Path` | `Yes` | (Required) gist_id parameter |

| `comment_id` | `string` | `Path` | `Yes` | (Required) comment_id parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


=== "404 Not Found"

    Resource Not Found

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "403 Forbidden"

    Forbidden Gist

    ```json
    {
     "block": {
      "reason": "qui",
      "created_at": "sint do",
      "html_url": "irure ipsum commodo"
     },
     "message": "lab",
     "documentation_url": "nisi enim"
    }
    ```


=== "200 OK"

    response

    ```json
    {
     "id": 1,
     "node_id": "MDExOkdpc3RDb21tZW50MQ==",
     "url": "https://api.github.com/gists/a6db0bec360bb87e9418/comments/1",
     "body": "Just commenting for the sake of commenting",
     "user": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
     },
     "created_at": "2011-04-18T23:23:56Z",
     "updated_at": "2011-04-18T23:23:56Z",
     "author_association": "collaborator"
    }
    ```


