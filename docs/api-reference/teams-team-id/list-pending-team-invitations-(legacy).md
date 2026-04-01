# List pending team invitations (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List pending team invitations`](https://developer.github.com/v3/teams/members/#list-pending-team-invitations) endpoint.

The return hash contains a `role` field which refers to the Organization Invitation role and will be one of the following values: `direct_member`, `admin`, `billing_manager`, `hiring_manager`, or `reinstate`. If the invitee is not a GitHub member, the `login` field in the return hash will be `null`.

```http
GET {{baseUrl}}/teams/:team_id/invitations?per_page=30&page=1
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


=== "200 OK"

    response

    ```json
    [
     {
      "id": 1,
      "login": "monalisa",
      "email": "octocat@github.com",
      "role": "direct_member",
      "created_at": "2016-11-30T06:46:10-08:00",
      "inviter": {
       "login": "other_user",
       "id": 1,
       "node_id": "MDQ6VXNlcjE=",
       "avatar_url": "https://github.com/images/error/other_user_happy.gif",
       "gravatar_id": "",
       "url": "https://api.github.com/users/other_user",
       "html_url": "https://github.com/other_user",
       "followers_url": "https://api.github.com/users/other_user/followers",
       "following_url": "https://api.github.com/users/other_user/following{/other_user}",
       "gists_url": "https://api.github.com/users/other_user/gists{/gist_id}",
       "starred_url": "https://api.github.com/users/other_user/starred{/owner}{/repo}",
       "subscriptions_url": "https://api.github.com/users/other_user/subscriptions",
       "organizations_url": "https://api.github.com/users/other_user/orgs",
       "repos_url": "https://api.github.com/users/other_user/repos",
       "events_url": "https://api.github.com/users/other_user/events{/privacy}",
       "received_events_url": "https://api.github.com/users/other_user/received_events",
       "type": "User",
       "site_admin": false
      },
      "team_count": 2,
      "invitation_team_url": "https://api.github.com/organizations/2/invitations/1/teams"
     }
    ]
    ```


