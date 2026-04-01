# List deploy keys



```http
GET {{baseUrl}}/repos/:owner/:repo/keys?per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

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
      "id": 1,
      "key": "ssh-rsa AAA...",
      "url": "https://api.github.com/repos/octocat/Hello-World/keys/1",
      "title": "octocat@octomac",
      "verified": true,
      "created_at": "2014-12-10T15:53:42Z",
      "read_only": true
     }
    ]
    ```


