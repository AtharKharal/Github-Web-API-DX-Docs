# Add or update team project permissions

Adds an organization project to a team. To add a project to a team or update the team's permission on a project, the authenticated user must have `admin` permissions for the project. The project and team must be part of the same organization.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `PUT /organizations/{org_id}/team/{team_id}/projects/{project_id}`.

```http
PUT {{baseUrl}}/orgs/:org/teams/:team_slug/projects/:project_id
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
    {
        "permission": "<string>"
    }
    ```


## Responses


=== "204 No Content"

    Empty response

    ```json
    
    ```


=== "403 Forbidden"

    Response if the project is not owned by the organization

    ```json
    {
     "message": "Must have admin rights to Repository.",
     "documentation_url": "https://developer.github.com/v3/teams/#add-or-update-team-project-permissions"
    }
    ```


