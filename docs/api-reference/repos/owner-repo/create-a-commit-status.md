# Create a commit status

Users with push access in a repository can create commit statuses for a given SHA.

Note: there is a limit of 1000 statuses per `sha` and `context` within a repository. Attempts to create more than 1000 statuses will result in a validation error.

```http
POST {{baseUrl}}/repos/:owner/:repo/statuses/:sha
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `sha` | `string` | `Path` | `Yes` | (Required) sha parameter |



## Request Body

=== "JSON"

    ```json
    {
        "state": "<string>",
        "target_url": "<string>",
        "description": "<string>",
        "context": "default"
    }
    ```


## Responses


=== "201 Created"

    response

    ```json
    {
     "url": "https://api.github.com/repos/octocat/Hello-World/statuses/6dcb09b5b57875f334f61aebed695e2e4193db5e",
     "avatar_url": "https://github.com/images/error/hubot_happy.gif",
     "id": 1,
     "node_id": "MDY6U3RhdHVzMQ==",
     "state": "success",
     "description": "Build has completed successfully",
     "target_url": "https://ci.example.com/1000/output",
     "context": "continuous-integration/jenkins",
     "created_at": "2012-07-20T01:19:13Z",
     "updated_at": "2012-07-20T01:19:13Z",
     "creator": {
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
     }
    }
    ```


