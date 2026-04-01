# Update a discussion comment

Edits the body text of a discussion comment. OAuth access tokens require the `write:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

**Note:** You can also specify a team by `org_id` and `team_id` using the route `PATCH /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments/{comment_number}`.

```http
PATCH {{baseUrl}}/orgs/:org/teams/:team_slug/discussions/:discussion_number/comments/:comment_number
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `org` | `string` | `Path` | `Yes` | (Required)  |

| `team_slug` | `string` | `Path` | `Yes` | (Required) team_slug parameter |

| `discussion_number` | `string` | `Path` | `Yes` | (Required)  |

| `comment_number` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    {
        "body": "<string>"
    }
    ```


## Responses


=== "200 OK"

    response

    ```json
    {
     "author": {
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
     "body": "Do you like pineapples?",
     "body_html": "<p>Do you like pineapples?</p>",
     "body_version": "e6907b24d9c93cc0c5024a7af5888116",
     "created_at": "2018-01-15T23:53:58Z",
     "last_edited_at": "2018-01-26T18:22:20Z",
     "discussion_url": "https://api.github.com/teams/2403582/discussions/1",
     "html_url": "https://github.com/orgs/github/teams/justice-league/discussions/1/comments/1",
     "node_id": "MDIxOlRlYW1EaXNjdXNzaW9uQ29tbWVudDE=",
     "number": 1,
     "updated_at": "2018-01-26T18:22:20Z",
     "url": "https://api.github.com/teams/2403582/discussions/1/comments/1",
     "reactions": {
      "url": "https://api.github.com/teams/2403582/discussions/1/reactions",
      "total_count": 5,
      "+1": 3,
      "-1": 1,
      "laugh": 0,
      "confused": 0,
      "heart": 1,
      "hooray": 0,
      "eyes": 1,
      "rocket": 1
     }
    }
    ```


