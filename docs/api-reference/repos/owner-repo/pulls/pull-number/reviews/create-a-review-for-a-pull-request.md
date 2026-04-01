# Create a review for a pull request

This endpoint triggers [notifications](https://help.github.com/articles/about-notifications/). Creating content too quickly using this endpoint may result in abuse rate limiting. See "[Abuse rate limits](https://developer.github.com/v3/#abuse-rate-limits)" and "[Dealing with abuse rate limits](https://developer.github.com/v3/guides/best-practices-for-integrators/#dealing-with-abuse-rate-limits)" for details.

Pull request reviews created in the `PENDING` state do not include the `submitted_at` property in the response.

**Note:** To comment on a specific line in a file, you need to first determine the _position_ of that line in the diff. The GitHub REST API v3 offers the `application/vnd.github.v3.diff` [media type](https://developer.github.com/v3/media/#commits-commit-comparison-and-pull-requests). To see a pull request diff, add this media type to the `Accept` header of a call to the [single pull request](https://developer.github.com/v3/pulls/#get-a-pull-request) endpoint.

The `position` value equals the number of lines down from the first "@@" hunk header in the file you want to add a comment. The line just below the "@@" line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file.

```http
POST {{baseUrl}}/repos/:owner/:repo/pulls/:pull_number/reviews
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `pull_number` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    {
        "commit_id": "<string>",
        "body": "<string>",
        "event": "<string>",
        "comments": [
            {
                "path": "<string>",
                "body": "<string>",
                "position": "<integer>",
                "line": "<integer>",
                "side": "<string>",
                "start_line": "<integer>",
                "start_side": "<string>"
            },
            {
                "path": "<string>",
                "body": "<string>",
                "position": "<integer>",
                "line": "<integer>",
                "side": "<string>",
                "start_line": "<integer>",
                "start_side": "<string>"
            }
        ]
    }
    ```


## Responses


=== "422 Unprocessable Entity (WebDAV) (RFC 4918)"

    Validation Failed

    ```json
    {
     "message": "in labore deserunt nostrud amet",
     "documentation_url": "Duis",
     "errors": [
      "nisi dolore Ut",
      "est culpa ullamco voluptate"
     ]
    }
    ```


=== "200 OK"

    response

    ```json
    {
     "id": 80,
     "node_id": "MDE3OlB1bGxSZXF1ZXN0UmV2aWV3ODA=",
     "user": {
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
     "body": "This is close to perfect! Please address the suggested inline change.",
     "state": "CHANGES_REQUESTED",
     "html_url": "https://github.com/octocat/Hello-World/pull/12#pullrequestreview-80",
     "pull_request_url": "https://api.github.com/repos/octocat/Hello-World/pulls/12",
     "_links": {
      "html": {
       "href": "https://github.com/octocat/Hello-World/pull/12#pullrequestreview-80"
      },
      "pull_request": {
       "href": "https://api.github.com/repos/octocat/Hello-World/pulls/12"
      }
     },
     "submitted_at": "2019-11-17T17:43:43Z",
     "commit_id": "ecdd80bb57125d7ba9641ffaa4d7d2c19d3f3091",
     "author_association": "collaborator"
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


