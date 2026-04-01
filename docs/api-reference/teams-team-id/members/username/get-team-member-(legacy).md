# Get team member (Legacy)

The "Get team member" endpoint (described below) is deprecated.

We recommend using the [Get team membership for a user](https://developer.github.com/v3/teams/members/#get-team-membership-for-a-user) endpoint instead. It allows you to get both active and pending memberships.

To list members in a team, the team must be visible to the authenticated user.

```http
GET {{baseUrl}}/teams/:team_id/members/:username
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `team_id` | `string` | `Path` | `Yes` | (Required)  |

| `username` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "204 No Content"

    Response if user is a member

    ```json
    
    ```


=== "404 Not Found"

    Response if user is not a member

    ```json
    
    ```


