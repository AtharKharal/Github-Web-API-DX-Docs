# Update a review for a pull request

Update the review summary comment with new text.

```http
PUT {{baseUrl}}/repos/:owner/:repo/pulls/:pull_number/reviews/:review_id
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `pull_number` | `string` | `Path` | `Yes` | (Required)  |

| `review_id` | `string` | `Path` | `Yes` | (Required) review_id parameter |



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
     "body": "This is close to perfect! Please address the suggested inline change. And add more about this.",
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


