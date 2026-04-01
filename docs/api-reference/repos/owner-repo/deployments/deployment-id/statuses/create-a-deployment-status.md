# Create a deployment status

Users with `push` access can create deployment statuses for a given deployment.

GitHub Apps require `read & write` access to "Deployments" and `read-only` access to "Repo contents" (for private repos). OAuth Apps require the `repo_deployment` scope.

```http
POST {{baseUrl}}/repos/:owner/:repo/deployments/:deployment_id/statuses
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `deployment_id` | `string` | `Path` | `Yes` | (Required) deployment_id parameter |



## Request Body

=== "JSON"

    ```json
    {
        "state": "<string>",
        "target_url": "",
        "log_url": "",
        "description": "",
        "environment": "<string>",
        "environment_url": "",
        "auto_inactive": "<boolean>"
    }
    ```


## Responses


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
     "url": "https://api.github.com/repos/octocat/example/deployments/42/statuses/1",
     "id": 1,
     "node_id": "MDE2OkRlcGxveW1lbnRTdGF0dXMx",
     "state": "success",
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
     },
     "description": "Deployment finished successfully.",
     "environment": "production",
     "target_url": "https://example.com/deployment/42/output",
     "created_at": "2012-07-20T01:19:13Z",
     "updated_at": "2012-07-20T01:19:13Z",
     "deployment_url": "https://api.github.com/repos/octocat/example/deployments/42",
     "repository_url": "https://api.github.com/repos/octocat/example",
     "environment_url": "https://test-branch.lab.acme.com",
     "log_url": "https://example.com/deployment/42/output"
    }
    ```


