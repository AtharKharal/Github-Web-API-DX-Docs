# Get a deploy key



```http
GET {{baseUrl}}/repos/:owner/:repo/keys/:key_id
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `key_id` | `string` | `Path` | `Yes` | (Required) key_id parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "404 Not Found"

    Resource Not Found

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
     "id": 1,
     "key": "ssh-rsa AAA...",
     "url": "https://api.github.com/repos/octocat/Hello-World/keys/1",
     "title": "octocat@octomac",
     "verified": true,
     "created_at": "2014-12-10T15:53:42Z",
     "read_only": true
    }
    ```


