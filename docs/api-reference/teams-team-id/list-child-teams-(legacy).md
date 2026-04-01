# List child teams (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List child teams`](https://developer.github.com/v3/teams/#list-child-teams) endpoint.

```http
GET {{baseUrl}}/teams/:team_id/teams?per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `team_id` | `string` | `Path` | `Yes` | (Required)  |

| `per_page` | `string` | `Query` | `No` | Results per page (max 100) |

| `page` | `string` | `Query` | `No` | Page number of the results to fetch. |



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


=== "403 Forbidden"

    Forbidden

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "200 OK"

    Response if child teams exist

    ```json
    [
     {
      "id": 2,
      "node_id": "MDQ6VGVhbTI=",
      "url": "https://api.github.com/teams/2",
      "name": "Original Roster",
      "slug": "original-roster",
      "description": "Started it all.",
      "privacy": "closed",
      "permission": "admin",
      "members_url": "https://api.github.com/teams/2/members{/member}",
      "repositories_url": "https://api.github.com/teams/2/repos",
      "parent": {
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
       "repositories_url": "https://api.github.com/teams/1/repos"
      },
      "html_url": "https://github.com/orgs/rails/teams/core"
     }
    ]
    ```


