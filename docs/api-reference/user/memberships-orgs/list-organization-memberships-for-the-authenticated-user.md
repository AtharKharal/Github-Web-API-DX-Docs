# List organization memberships for the authenticated user



```http
GET {{baseUrl}}/user/memberships/orgs?state=<string>&per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `state` | `string` | `Query` | `No` | Indicates the state of the memberships to return. Can be either `active` or `pending`. If not specified, the API returns both active and pending memberships. |

| `per_page` | `string` | `Query` | `No` | Results per page (max 100) |

| `page` | `string` | `Query` | `No` | Page number of the results to fetch. |



## Request Body

=== "JSON"

    ```json
    
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


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


=== "401 Unauthorized"

    Requires Authentication

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
    [
     {
      "url": "https://api.github.com/orgs/octocat/memberships/defunkt",
      "state": "active",
      "role": "admin",
      "organization_url": "https://api.github.com/orgs/octocat",
      "organization": {
       "login": "github",
       "id": 1,
       "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
       "url": "https://api.github.com/orgs/github",
       "repos_url": "https://api.github.com/orgs/github/repos",
       "events_url": "https://api.github.com/orgs/github/events",
       "hooks_url": "https://api.github.com/orgs/github/hooks",
       "issues_url": "https://api.github.com/orgs/github/issues",
       "members_url": "https://api.github.com/orgs/github/members{/member}",
       "public_members_url": "https://api.github.com/orgs/github/public_members{/member}",
       "avatar_url": "https://github.com/images/error/octocat_happy.gif",
       "description": "A great organization"
      },
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
      }
     },
     {
      "url": "https://api.github.com/orgs/invitocat/memberships/defunkt",
      "state": "pending",
      "role": "admin",
      "organization_url": "https://api.github.com/orgs/invitocat",
      "organization": {
       "login": "github",
       "id": 1,
       "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
       "url": "https://api.github.com/orgs/github",
       "repos_url": "https://api.github.com/orgs/github/repos",
       "events_url": "https://api.github.com/orgs/github/events",
       "hooks_url": "https://api.github.com/orgs/github/hooks",
       "issues_url": "https://api.github.com/orgs/github/issues",
       "members_url": "https://api.github.com/orgs/github/members{/member}",
       "public_members_url": "https://api.github.com/orgs/github/public_members{/member}",
       "avatar_url": "https://github.com/images/error/octocat_happy.gif",
       "description": "A great organization"
      },
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
      }
     }
    ]
    ```


