# List discussions (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List discussions`](https://developer.github.com/v3/teams/discussions/#list-discussions) endpoint.

List all discussions on a team's page. OAuth access tokens require the `read:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

```http
GET {{baseUrl}}/teams/:team_id/discussions?direction=desc&per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `team_id` | `string` | `Path` | `Yes` | (Required)  |

| `direction` | `string` | `Query` | `No` | One of `asc` (ascending) or `desc` (descending). |

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
      "body": "Hi! This is an area for us to collaborate as a team.",
      "body_html": "<p>Hi! This is an area for us to collaborate as a team</p>",
      "body_version": "0d495416a700fb06133c612575d92bfb",
      "comments_count": 0,
      "comments_url": "https://api.github.com/teams/2343027/discussions/1/comments",
      "created_at": "2018-01-25T18:56:31Z",
      "last_edited_at": null,
      "html_url": "https://github.com/orgs/github/teams/justice-league/discussions/1",
      "node_id": "MDE0OlRlYW1EaXNjdXNzaW9uMQ==",
      "number": 1,
      "pinned": false,
      "private": false,
      "team_url": "https://api.github.com/teams/2343027",
      "title": "Our first team post",
      "updated_at": "2018-01-25T18:56:31Z",
      "url": "https://api.github.com/teams/2343027/discussions/1",
      "reactions": {
       "url": "https://api.github.com/teams/2343027/discussions/1/reactions",
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
    ]
    ```


