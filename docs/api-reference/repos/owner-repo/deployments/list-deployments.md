# List deployments

Simple filtering of deployments is available via query parameters:

```http
GET {{baseUrl}}/repos/:owner/:repo/deployments?sha=none&ref=none&task=none&environment=none&per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `sha` | `string` | `Query` | `No` | The SHA recorded at creation time. |

| `ref` | `string` | `Query` | `No` | The name of the ref. This can be a branch, tag, or SHA. |

| `task` | `string` | `Query` | `No` | The name of the task for the deployment (e.g., `deploy` or `deploy:migrations`). |

| `environment` | `string` | `Query` | `No` | The name of the environment that was deployed to (e.g., `staging` or `production`). |

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
      "url": "https://api.github.com/repos/octocat/example/deployments/1",
      "id": 1,
      "node_id": "MDEwOkRlcGxveW1lbnQx",
      "sha": "a84d88e7554fc1fa21bcbc4efae3c782a70d2b9d",
      "ref": "topic-branch",
      "task": "deploy",
      "payload": {},
      "original_environment": "staging",
      "environment": "production",
      "description": "Deploy request from hubot",
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
      "created_at": "2012-07-20T01:19:13Z",
      "updated_at": "2012-07-20T01:19:13Z",
      "statuses_url": "https://api.github.com/repos/octocat/example/deployments/1/statuses",
      "repository_url": "https://api.github.com/repos/octocat/example",
      "transient_environment": false,
      "production_environment": true
     }
    ]
    ```


