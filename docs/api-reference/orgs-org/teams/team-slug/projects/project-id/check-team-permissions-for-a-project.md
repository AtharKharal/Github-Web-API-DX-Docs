# Check team permissions for a project

Checks whether a team has `read`, `write`, or `admin` permissions for an organization project. The response includes projects inherited from a parent team.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/projects/{project_id}`.

```http
GET {{baseUrl}}/orgs/:org/teams/:team_slug/projects/:project_id
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `org` | `string` | `Path` | `Yes` | (Required)  |

| `team_slug` | `string` | `Path` | `Yes` | (Required) team_slug parameter |

| `project_id` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "200 OK"

    response

    ```json
    {
     "owner_url": "https://api.github.com/orgs/octocat",
     "url": "https://api.github.com/projects/1002605",
     "html_url": "https://github.com/orgs/api-playground/projects/1",
     "columns_url": "https://api.github.com/projects/1002605/columns",
     "id": 1002605,
     "node_id": "MDc6UHJvamVjdDEwMDI2MDU=",
     "name": "Organization Roadmap",
     "body": "High-level roadmap for the upcoming year.",
     "number": 1,
     "state": "open",
     "creator": {
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
     "created_at": "2011-04-11T20:09:31Z",
     "updated_at": "2014-03-04T18:58:10Z",
     "organization_permission": "write",
     "private": false,
     "permissions": {
      "read": true,
      "write": true,
      "admin": false
     }
    }
    ```


=== "404 Not Found"

    Response if project is not managed by this team

    ```json
    
    ```


