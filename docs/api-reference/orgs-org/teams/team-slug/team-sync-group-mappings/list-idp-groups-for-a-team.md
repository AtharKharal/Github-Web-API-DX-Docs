# List IdP groups for a team

Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

List IdP groups connected to a team on GitHub.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/team-sync/group-mappings`.

```http
GET {{baseUrl}}/orgs/:org/teams/:team_slug/team-sync/group-mappings
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `org` | `string` | `Path` | `Yes` | (Required)  |

| `team_slug` | `string` | `Path` | `Yes` | (Required) team_slug parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "200 OK"

    response

    ```json
    {
     "groups": [
      {
       "group_id": "123",
       "group_name": "Octocat admins",
       "group_description": "The people who configure your octoworld."
      },
      {
       "group_id": "456",
       "group_name": "Octocat docs members",
       "group_description": "The people who make your octoworld come to life."
      }
     ]
    }
    ```


