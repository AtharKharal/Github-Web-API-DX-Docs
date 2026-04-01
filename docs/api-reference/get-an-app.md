# Get an app

**Note**: The `:app_slug` is just the URL-friendly name of your GitHub App. You can find this on the settings page for your GitHub App (e.g., `https://github.com/settings/apps/:app_slug`).

If the GitHub App you specify is public, you can access this endpoint without authenticating. If the GitHub App you specify is private, you must authenticate with a [personal access token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) or an [installation access token](https://developer.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-an-installation) to access this endpoint.

```http
GET {{baseUrl}}/apps/:app_slug
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `app_slug` | `string` | `Path` | `Yes` | (Required) app_slug parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "415 Unsupported Media Type"

    Preview Header Missing

    ```json
    {
     "message": "enim velit officia",
     "documentation_url": "et proident"
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


=== "403 Forbidden"

    Forbidden

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
    ```


