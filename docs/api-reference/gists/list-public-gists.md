# List public gists

List public gists sorted by most recently updated to least recently updated.

Note: With [pagination](https://developer.github.com/v3/#pagination), you can fetch up to 3000 gists. For example, you can fetch 100 pages with 30 gists per page or 30 pages with 100 gists per page.

```http
GET {{baseUrl}}/gists/public?since=<string>&per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `since` | `string` | `Query` | `No` | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. |

| `per_page` | `string` | `Query` | `No` | Results per page (max 100) |

| `page` | `string` | `Query` | `No` | Page number of the results to fetch. |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


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


=== "200 OK"

    response

    ```json
    [
     {
      "url": "https://api.github.com/gists/aa5a315d61ae9438b18d",
      "forks_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/forks",
      "commits_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/commits",
      "id": "aa5a315d61ae9438b18d",
      "node_id": "MDQ6R2lzdGFhNWEzMTVkNjFhZTk0MzhiMThk",
      "git_pull_url": "https://gist.github.com/aa5a315d61ae9438b18d.git",
      "git_push_url": "https://gist.github.com/aa5a315d61ae9438b18d.git",
      "html_url": "https://gist.github.com/aa5a315d61ae9438b18d",
      "files": {
       "hello_world.rb": {
        "filename": "hello_world.rb",
        "type": "application/x-ruby",
        "language": "Ruby",
        "raw_url": "https://gist.githubusercontent.com/octocat/6cad326836d38bd3a7ae/raw/db9c55113504e46fa076e7df3a04ce592e2e86d8/hello_world.rb",
        "size": 167
       }
      },
      "public": true,
      "created_at": "2010-04-14T02:15:15Z",
      "updated_at": "2011-06-20T11:34:15Z",
      "description": "Hello World Examples",
      "comments": 0,
      "user": null,
      "comments_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/comments/",
      "owner": {
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
      "truncated": false
     }
    ]
    ```


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


=== "403 Forbidden"

    Forbidden

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


