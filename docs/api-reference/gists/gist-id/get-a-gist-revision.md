# Get a gist revision



```http
GET {{baseUrl}}/gists/:gist_id/:sha
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `gist_id` | `string` | `Path` | `Yes` | (Required) gist_id parameter |

| `sha` | `string` | `Path` | `Yes` | (Required) sha parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "403 Forbidden"

    Forbidden

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "200 OK"

    response

    ```json
    {
     "url": "https://api.github.com/gists/aa5a315d61ae9438b18d/57a7f021a713b1c5a6a199b54cc514735d2d462f",
     "forks_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/forks",
     "commits_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/commits",
     "id": "aa5a315d61ae9438b18d",
     "node_id": "MDQ6R2lzdGFhNWEzMTVkNjFhZTk0MzhiMThk",
     "git_pull_url": "https://gist.github.com/aa5a315d61ae9438b18d.git",
     "git_push_url": "https://gist.github.com/aa5a315d61ae9438b18d.git",
     "html_url": "https://gist.github.com/aa5a315d61ae9438b18d",
     "created_at": "2010-04-14T02:15:15Z",
     "updated_at": "2011-06-20T11:34:15Z",
     "description": "Hello World Examples",
     "comments": 0,
     "comments_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/comments/"
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


