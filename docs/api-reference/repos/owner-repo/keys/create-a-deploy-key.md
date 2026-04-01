# Create a deploy key

You can create a read-only deploy key.

```http
POST {{baseUrl}}/repos/:owner/:repo/keys
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    {
        "key": "<string>",
        "title": "<string>",
        "read_only": "<boolean>"
    }
    ```


## Responses


=== "201 Created"

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


