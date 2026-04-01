# List review comments in a repository

**Note:** Multi-line comments on pull requests are currently in public beta and subject to change.

Lists review comments for all pull requests in a repository. By default, review comments are in ascending order by ID.

**Multi-line comment summary**

**Note:** New parameters and response fields are available for developers to preview. During the preview period, these response fields may change without advance notice. Please see the [blog post](https://developer.github.com/changes/2019-10-03-multi-line-comments) for full details.

Use the `comfort-fade` preview header and the `line` parameter to show multi-line comment-supported fields in the response.

If you use the `comfort-fade` preview header, your response will show:

*   For multi-line comments, values for `start_line`, `original_start_line`, `start_side`, `line`, `original_line`, and `side`.
*   For single-line comments, values for `line`, `original_line`, and `side` and a `null` value for `start_line`, `original_start_line`, and `start_side`.

If you don't use the `comfort-fade` preview header, multi-line and single-line comments will appear the same way in the response with a single `position` attribute. Your response will show:

*   For multi-line comments, the last line of the comment range for the `position` attribute.
*   For single-line comments, the diff-positioned way of referencing comments for the `position` attribute. For more information, see `position` in the [input parameters](https://developer.github.com/v3/pulls/comments/#parameters-2) table.

The `reactions` key will have the following payload where `url` can be used to construct the API location for [listing and creating](https://developer.github.com/v3/reactions) reactions.

```http
GET {{baseUrl}}/repos/:owner/:repo/pulls/comments?sort=created&direction=<string>&since=<string>&per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `sort` | `string` | `Query` | `No` | One of `created` (when the repository was starred) or `updated` (when it was last pushed to). |

| `direction` | `string` | `Query` | `No` | Can be either `asc` or `desc`. Ignored without `sort` parameter. |

| `since` | `string` | `Query` | `No` | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. |

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
      "url": "https://api.github.com/repos/octocat/Hello-World/pulls/comments/1",
      "pull_request_review_id": 42,
      "id": 10,
      "node_id": "MDI0OlB1bGxSZXF1ZXN0UmV2aWV3Q29tbWVudDEw",
      "diff_hunk": "@@ -16,33 +16,40 @@ public class Connection : IConnection...",
      "path": "file1.txt",
      "position": 1,
      "original_position": 4,
      "commit_id": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
      "original_commit_id": "9c48853fa3dc5c1c3d6f1f1cd1f2743e72652840",
      "in_reply_to_id": 8,
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
      "body": "Great stuff!",
      "created_at": "2011-04-14T16:00:49Z",
      "updated_at": "2011-04-14T16:00:49Z",
      "html_url": "https://github.com/octocat/Hello-World/pull/1#discussion-diff-1",
      "pull_request_url": "https://api.github.com/repos/octocat/Hello-World/pulls/1",
      "author_association": "NONE",
      "_links": {
       "self": {
        "href": "https://api.github.com/repos/octocat/Hello-World/pulls/comments/1"
       },
       "html": {
        "href": "https://github.com/octocat/Hello-World/pull/1#discussion-diff-1"
       },
       "pull_request": {
        "href": "https://api.github.com/repos/octocat/Hello-World/pulls/1"
       }
      },
      "start_line": 1,
      "original_start_line": 1,
      "start_side": "RIGHT",
      "line": 2,
      "original_line": 2,
      "side": "RIGHT"
     }
    ]
    ```


