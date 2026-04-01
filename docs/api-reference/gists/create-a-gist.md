# Create a gist

Allows you to add a new gist with one or more files.

**Note:** Don't name your files "gistfile" with a numerical suffix. This is the format of the automatic naming scheme that Gist uses internally.

```http
POST {{baseUrl}}/gists
```





## Request Body

=== "JSON"

    ```json
    {
        "files": "<object>",
        "description": "<string>",
        "public": false
    }
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


=== "404 Not Found"

    Resource Not Found

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
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
     "created_at": "2010-04-14T02:15:15Z",
     "updated_at": "2011-06-20T11:34:15Z",
     "description": "Hello World Examples",
     "comments": 0,
     "comments_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/comments/"
    }
    ```


