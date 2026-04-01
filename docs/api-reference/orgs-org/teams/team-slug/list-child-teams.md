# List child teams

Lists the child teams of the team specified by `{team_slug}`.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/teams`.

```http
GET {{baseUrl}}/orgs/:org/teams/:team_slug/teams?per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `org` | `string` | `Path` | `Yes` | (Required)  |

| `team_slug` | `string` | `Path` | `Yes` | (Required) team_slug parameter |

| `per_page` | `string` | `Query` | `No` | Results per page (max 100) |

| `page` | `string` | `Query` | `No` | Page number of the results to fetch. |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


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


