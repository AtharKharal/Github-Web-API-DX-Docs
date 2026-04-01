# Fork a gist

**Note**: This was previously `/gists/:gist_id/fork`.

```http
POST {{baseUrl}}/gists/:gist_id/forks
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `gist_id` | `string` | `Path` | `Yes` | (Required) gist_id parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


=== "201 Created"

    response

    ```json
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


=== "404 Not Found"

    Resource Not Found

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
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


