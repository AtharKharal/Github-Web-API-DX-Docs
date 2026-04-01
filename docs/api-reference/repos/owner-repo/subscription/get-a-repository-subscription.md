# Get a repository subscription



```http
GET {{baseUrl}}/repos/:owner/:repo/subscription
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "200 OK"

    Response if you subscribe to the repository

    ```json
    {
     "subscribed": true,
     "ignored": false,
     "reason": null,
     "created_at": "2012-10-06T21:34:12Z",
     "url": "https://api.github.com/repos/octocat/example/subscription",
     "repository_url": "https://api.github.com/repos/octocat/example"
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


=== "404 Not Found"

    Response if you don't subscribe to the repository

    ```json
    
    ```


