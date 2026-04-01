# List teams for the authenticated user

List all of the teams across all of the organizations to which the authenticated user belongs. This method requires `user`, `repo`, or `read:org` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/) when authenticating via [OAuth](https://developer.github.com/apps/building-oauth-apps/).

```http
GET {{baseUrl}}/user/teams?per_page=30&page=1
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


=== "403 Forbidden"

    Forbidden

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
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


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


=== "200 OK"

    response

    ```json
    [
     {
      "id": 1,
      "node_id": "MDQ6VGVhbTE=",
      "url": "https://api.github.com/teams/1",
      "html_url": "https://api.github.com/teams/justice-league",
      "name": "Justice League",
      "slug": "justice-league",
      "description": "A great team.",
      "privacy": "closed",
      "permission": "admin",
      "members_url": "https://api.github.com/teams/1/members{/member}",
      "repositories_url": "https://api.github.com/teams/1/repos",
      "parent": null,
      "members_count": 3,
      "repos_count": 10,
      "created_at": "2017-07-14T16:53:42Z",
      "updated_at": "2017-08-17T12:37:15Z",
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
       "description": "A great organization",
       "name": "github",
       "company": "GitHub",
       "blog": "https://github.com/blog",
       "location": "San Francisco",
       "email": "octocat@github.com",
       "is_verified": true,
       "has_organization_projects": true,
       "has_repository_projects": true,
       "public_repos": 2,
       "public_gists": 1,
       "followers": 20,
       "following": 0,
       "html_url": "https://github.com/octocat",
       "created_at": "2008-01-14T04:33:35Z",
       "updated_at": "2017-08-17T12:37:15Z",
       "type": "Organization"
      }
     }
    ]
    ```


