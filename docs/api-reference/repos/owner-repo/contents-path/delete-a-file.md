# Delete a file

Deletes a file in a repository.

You can provide an additional `committer` parameter, which is an object containing information about the committer. Or, you can provide an `author` parameter, which is an object containing information about the author.

The `author` section is optional and is filled in with the `committer` information if omitted. If the `committer` information is omitted, the authenticated user's information is used.

You must provide values for both `name` and `email`, whether you choose to use `author` or `committer`. Otherwise, you'll receive a `422` status code.

```http
DELETE {{baseUrl}}/repos/:owner/:repo/contents/:path
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `path` | `string` | `Path` | `Yes` | (Required) path+ parameter |



## Request Body

=== "JSON"

    ```json
    {
        "message": "<string>",
        "sha": "<string>",
        "branch": "<string>",
        "committer": {
            "name": "<string>",
            "email": "<string>"
        },
        "author": {
            "name": "<string>",
            "email": "<string>"
        }
    }
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
     "content": null,
     "commit": {
      "sha": "7638417db6d59f3c431d3e1f261cc637155684cd",
      "node_id": "MDY6Q29tbWl0NzYzODQxN2RiNmQ1OWYzYzQzMWQzZTFmMjYxY2M2MzcxNTU2ODRjZA==",
      "url": "https://api.github.com/repos/octocat/Hello-World/git/commits/7638417db6d59f3c431d3e1f261cc637155684cd",
      "html_url": "https://github.com/octocat/Hello-World/git/commit/7638417db6d59f3c431d3e1f261cc637155684cd",
      "author": {
       "date": "2014-11-07T22:01:45Z",
       "name": "Monalisa Octocat",
       "email": "octocat@github.com"
      },
      "committer": {
       "date": "2014-11-07T22:01:45Z",
       "name": "Monalisa Octocat",
       "email": "octocat@github.com"
      },
      "message": "my commit message",
      "tree": {
       "url": "https://api.github.com/repos/octocat/Hello-World/git/trees/691272480426f78a0138979dd3ce63b77f706feb",
       "sha": "691272480426f78a0138979dd3ce63b77f706feb"
      },
      "parents": [
       {
        "url": "https://api.github.com/repos/octocat/Hello-World/git/commits/1acc419d4d6a9ce985db7be48c6349a0475975b5",
        "html_url": "https://github.com/octocat/Hello-World/git/commit/1acc419d4d6a9ce985db7be48c6349a0475975b5",
        "sha": "1acc419d4d6a9ce985db7be48c6349a0475975b5"
       }
      ],
      "verification": {
       "verified": false,
       "reason": "unsigned",
       "signature": null,
       "payload": null
      }
     }
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


=== "409 Conflict"

    Conflict

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "503 Service Unavailable"

    Service Unavailable

    ```json
    {
     "code": "nisi",
     "message": "enim amet nostrud",
     "documentation_url": "reprehenderit id"
    }
    ```


