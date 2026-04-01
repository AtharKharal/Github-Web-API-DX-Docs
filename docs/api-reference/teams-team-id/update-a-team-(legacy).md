# Update a team (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Update a team](https://developer.github.com/v3/teams/#update-a-team) endpoint.

To edit a team, the authenticated user must either be an organization owner or a team maintainer.

**Note:** With nested teams, the `privacy` for parent teams cannot be `secret`.

```http
PATCH {{baseUrl}}/teams/:team_id
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `team_id` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    {
        "name": "<string>",
        "description": "<string>",
        "privacy": "<string>",
        "permission": "pull",
        "parent_team_id": "<integer>"
    }
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
    ```


=== "404 Not Found"

    Resource Not Found

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


