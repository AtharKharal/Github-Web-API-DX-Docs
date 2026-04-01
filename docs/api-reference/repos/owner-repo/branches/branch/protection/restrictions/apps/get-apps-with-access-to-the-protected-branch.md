# Get apps with access to the protected branch

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Lists the GitHub Apps that have push access to this branch. Only installed GitHub Apps with `write` access to the `contents` permission can be added as authorized actors on a protected branch.

```http
GET {{baseUrl}}/repos/:owner/:repo/branches/:branch/protection/restrictions/apps
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `branch` | `string` | `Path` | `Yes` | (Required) branch+ parameter |



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
      "id": 1,
      "slug": "octoapp",
      "node_id": "MDExOkludGVncmF0aW9uMQ==",
      "owner": {
       "login": "github",
       "id": 1,
       "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
       "url": "https://api.github.com/orgs/github",
       "repos_url": "https://api.github.com/orgs/github/repos",
       "events_url": "https://api.github.com/orgs/github/events",
       "avatar_url": "https://github.com/images/error/octocat_happy.gif",
       "gravatar_id": "",
       "html_url": "https://github.com/octocat",
       "followers_url": "https://api.github.com/users/octocat/followers",
       "following_url": "https://api.github.com/users/octocat/following{/other_user}",
       "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
       "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
       "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
       "organizations_url": "https://api.github.com/users/octocat/orgs",
       "received_events_url": "https://api.github.com/users/octocat/received_events",
       "type": "User",
       "site_admin": true
      },
      "name": "Octocat App",
      "description": "",
      "external_url": "https://example.com",
      "html_url": "https://github.com/apps/octoapp",
      "created_at": "2017-07-08T16:18:44-04:00",
      "updated_at": "2017-07-08T16:18:44-04:00",
      "permissions": {
       "metadata": "read",
       "contents": "read",
       "issues": "write",
       "single_file": "write"
      },
      "events": [
       "push",
       "pull_request"
      ]
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


