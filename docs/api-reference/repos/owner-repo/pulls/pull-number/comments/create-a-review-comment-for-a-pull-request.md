# Create a review comment for a pull request

**Note:** Multi-line comments on pull requests are currently in public beta and subject to change.

Creates a review comment in the pull request diff. To add a regular comment to a pull request timeline, see "[Create an issue comment](https://developer.github.com/v3/issues/comments/#create-an-issue-comment)." We recommend creating a review comment using `line`, `side`, and optionally `start_line` and `start_side` if your comment applies to more than one line in the pull request diff.

You can still create a review comment using the `position` parameter. When you use `position`, the `line`, `side`, `start_line`, and `start_side` parameters are not required. For more information, see [Multi-line comment summary](https://developer.github.com/v3/pulls/comments/#multi-line-comment-summary-3).

**Note:** The position value equals the number of lines down from the first "@@" hunk header in the file you want to add a comment. The line just below the "@@" line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file.

This endpoint triggers [notifications](https://help.github.com/articles/about-notifications/). Creating content too quickly using this endpoint may result in abuse rate limiting. See "[Abuse rate limits](https://developer.github.com/v3/#abuse-rate-limits)" and "[Dealing with abuse rate limits](https://developer.github.com/v3/guides/best-practices-for-integrators/#dealing-with-abuse-rate-limits)" for details.

**Multi-line comment summary**

**Note:** New parameters and response fields are available for developers to preview. During the preview period, these response fields may change without advance notice. Please see the [blog post](https://developer.github.com/changes/2019-10-03-multi-line-comments) for full details.

Use the `comfort-fade` preview header and the `line` parameter to show multi-line comment-supported fields in the response.

If you use the `comfort-fade` preview header, your response will show:

*   For multi-line comments, values for `start_line`, `original_start_line`, `start_side`, `line`, `original_line`, and `side`.
*   For single-line comments, values for `line`, `original_line`, and `side` and a `null` value for `start_line`, `original_start_line`, and `start_side`.

If you don't use the `comfort-fade` preview header, multi-line and single-line comments will appear the same way in the response with a single `position` attribute. Your response will show:

*   For multi-line comments, the last line of the comment range for the `position` attribute.
*   For single-line comments, the diff-positioned way of referencing comments for the `position` attribute. For more information, see `position` in the [input parameters](https://developer.github.com/v3/pulls/comments/#parameters-2) table.

```http
POST {{baseUrl}}/repos/:owner/:repo/pulls/:pull_number/comments
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
        "body": "<string>",
        "path": "<string>",
        "commit_id": "<string>",
        "position": "<integer>",
        "side": "<string>",
        "line": "<integer>",
        "start_line": "<integer>",
        "start_side": "<string>",
        "in_reply_to": "<integer>"
    }
    ```


## Responses


=== "201 Created"

    response

    ```json
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
    ```


=== "403 Forbidden"

    Forbidden

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "422 Unprocessable Entity (WebDAV) (RFC 4918)"

    Validation Failed

    ```json
    {
     "message": "culpa mollit",
     "documentation_url": "ipsum ut",
     "errors": [
      {
       "code": "consequat enim et velit",
       "resource": "anim ullamco",
       "field": "voluptate officia amet",
       "message": "exercitation sed dolore est",
       "index": 18359415,
       "value": "ullamco ut velit nulla eiusmod"
      },
      {
       "code": "occaecat eiusmod Duis",
       "resource": "esse ad Excepteur mollit",
       "field": "minim ipsum nisi exercitation non",
       "message": "proident reprehenderit",
       "index": -23326731,
       "value": "adipisicing cupidatat culpa in"
      }
     ]
    }
    ```


