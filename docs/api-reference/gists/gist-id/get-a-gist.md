# Get a gist



```http
GET {{baseUrl}}/gists/:gist_id
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


=== "200 OK"

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


=== "404 Not Found"

    Resource Not Found

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "403 Forbidden"

    Forbidden Gist

    ```json
    {
     "block": {
      "reason": "qui",
      "created_at": "sint do",
      "html_url": "irure ipsum commodo"
     },
     "message": "lab",
     "documentation_url": "nisi enim"
    }
    ```


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


