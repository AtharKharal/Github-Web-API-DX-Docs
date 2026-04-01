# Get a repository installation for the authenticated app

Enables an authenticated GitHub App to find the repository's installation information. The installation's account type will be either an organization or a user account, depending which account the repository belongs to.

You must use a [JWT](https://developer.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

```http
GET {{baseUrl}}/repos/:owner/:repo/installation
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    
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


=== "200 OK"

    response

    ```json
    {
     "id": 1,
     "account": {
      "login": "github",
      "id": 1,
      "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
      "avatar_url": "https://github.com/images/error/hubot_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/orgs/github",
      "html_url": "https://github.com/github",
      "followers_url": "https://api.github.com/users/github/followers",
      "following_url": "https://api.github.com/users/github/following{/other_user}",
      "gists_url": "https://api.github.com/users/github/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/github/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/github/subscriptions",
      "organizations_url": "https://api.github.com/users/github/orgs",
      "repos_url": "https://api.github.com/orgs/github/repos",
      "events_url": "https://api.github.com/orgs/github/events",
      "received_events_url": "https://api.github.com/users/github/received_events",
      "type": "Organization",
      "site_admin": false
     },
     "repository_selection": "all",
     "access_tokens_url": "https://api.github.com/installations/1/access_tokens",
     "repositories_url": "https://api.github.com/installation/repositories",
     "html_url": "https://github.com/organizations/github/settings/installations/1",
     "app_id": 1,
     "target_id": 1,
     "target_type": "Organization",
     "permissions": {
      "checks": "write",
      "metadata": "read",
      "contents": "read"
     },
     "events": [
      "push",
      "pull_request"
     ],
     "created_at": "2018-02-09T20:51:14Z",
     "updated_at": "2018-02-09T20:51:14Z",
     "single_file_name": null,
     "app_slug": "github-actions"
    }
    ```


=== "301 Moved Permanently"

    Moved Permanently

    ```json
    
    ```


