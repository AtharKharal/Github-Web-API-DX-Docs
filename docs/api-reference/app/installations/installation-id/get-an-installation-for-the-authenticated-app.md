# Get an installation for the authenticated app

Enables an authenticated GitHub App to find an installation's information using the installation id. The installation's account type (`target_type`) will be either an organization or a user account, depending which account the repository belongs to.

You must use a [JWT](https://developer.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

```http
GET {{baseUrl}}/app/installations/:installation_id
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `installation_id` | `string` | `Path` | `Yes` | (Required) installation_id parameter |



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


=== "200 OK"

    response

    ```json
    {
     "id": 1,
     "account": {
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
     "single_file_name": "config.yml",
     "repository_selection": "selected",
     "created_at": "2017-07-08T16:18:44-04:00",
     "updated_at": "2017-07-08T16:18:44-04:00",
     "app_slug": "github-actions"
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


