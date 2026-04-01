# Create a discussion (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`Create a discussion`](https://developer.github.com/v3/teams/discussions/#create-a-discussion) endpoint.

Creates a new discussion post on a team's page. OAuth access tokens require the `write:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

This endpoint triggers [notifications](https://help.github.com/articles/about-notifications/). Creating content too quickly using this endpoint may result in abuse rate limiting. See "[Abuse rate limits](https://developer.github.com/v3/#abuse-rate-limits)" and "[Dealing with abuse rate limits](https://developer.github.com/v3/guides/best-practices-for-integrators/#dealing-with-abuse-rate-limits)" for details.

```http
POST {{baseUrl}}/teams/:team_id/discussions
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `team_id` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    {
        "title": "<string>",
        "body": "<string>",
        "private": false
    }
    ```


## Responses


=== "201 Created"

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
    ```


