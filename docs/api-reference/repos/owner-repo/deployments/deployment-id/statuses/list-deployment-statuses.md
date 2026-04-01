# List deployment statuses

Users with pull access can view deployment statuses for a deployment:

```http
GET {{baseUrl}}/repos/:owner/:repo/deployments/:deployment_id/statuses?per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `deployment_id` | `string` | `Path` | `Yes` | (Required) deployment_id parameter |

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


