# List app installations accessible to the user access token

Lists installations of your GitHub App that the authenticated user has explicit permission (`:read`, `:write`, or `:admin`) to access.

You must use a [user-to-server OAuth access token](https://developer.github.com/apps/building-github-apps/identifying-and-authorizing-users-for-github-apps/#identifying-users-on-your-site), created for a user who has authorized your GitHub App, to access this endpoint.

The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership.

You can find the permissions for the installation under the `permissions` key.

```http
GET {{baseUrl}}/user/installations?per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `per_page` | `string` | `Query` | `No` | Results per page (max 100) |

| `page` | `string` | `Query` | `No` | Page number of the results to fetch. |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "401 Unauthorized"

    Requires Authentication

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "415 Unsupported Media Type"

    Preview Header Missing

    ```json
    {
     "message": "enim velit officia",
     "documentation_url": "et proident"
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


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


=== "200 OK"

    You can find the permissions for the installation under the `permissions` key.

    ```json
    {
     "total_count": 2,
     "installations": [
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
       "repository_selection": "all",
       "created_at": "2017-07-08T16:18:44-04:00",
       "updated_at": "2017-07-08T16:18:44-04:00",
       "app_slug": "github-actions"
      },
      {
       "id": 3,
       "account": {
        "login": "octocat",
        "id": 2,
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
       "repository_selection": "all",
       "created_at": "2017-07-08T16:18:44-04:00",
       "updated_at": "2017-07-08T16:18:44-04:00",
       "app_slug": "github-actions"
      }
     ]
    }
    ```


