# Create or update file contents

Creates a new file or replaces an existing file in a repository.

```http
PUT {{baseUrl}}/repos/:owner/:repo/contents/:path
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
        "content": "<string>",
        "sha": "<string>",
        "branch": "<string>",
        "committer": {
            "name": "<string>",
            "email": "<string>",
            "date": "<string>"
        },
        "author": {
            "name": "<string>",
            "email": "<string>",
            "date": "<string>"
        }
    }
    ```


## Responses


=== "409 Conflict"

    Conflict

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
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


=== "201 Created"

    response

    ```json
    {
     "content": {
      "name": "hello.txt",
      "path": "notes/hello.txt",
      "sha": "95b966ae1c166bd92f8ae7d1c313e738c731dfc3",
      "size": 9,
      "url": "https://api.github.com/repos/octocat/Hello-World/contents/notes/hello.txt",
      "html_url": "https://github.com/octocat/Hello-World/blob/master/notes/hello.txt",
      "git_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs/95b966ae1c166bd92f8ae7d1c313e738c731dfc3",
      "download_url": "https://raw.githubusercontent.com/octocat/HelloWorld/master/notes/hello.txt",
      "type": "file",
      "_links": {
       "self": "https://api.github.com/repos/octocat/Hello-World/contents/notes/hello.txt",
       "git": "https://api.github.com/repos/octocat/Hello-World/git/blobs/95b966ae1c166bd92f8ae7d1c313e738c731dfc3",
       "html": "https://github.com/octocat/Hello-World/blob/master/notes/hello.txt"
      }
     },
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


=== "200 OK"

    response

    ```json
    {
     "content": {
      "name": "hello.txt",
      "path": "notes/hello.txt",
      "sha": "a56507ed892d05a37c6d6128c260937ea4d287bd",
      "size": 9,
      "url": "https://api.github.com/repos/octocat/Hello-World/contents/notes/hello.txt",
      "html_url": "https://github.com/octocat/Hello-World/blob/master/notes/hello.txt",
      "git_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs/a56507ed892d05a37c6d6128c260937ea4d287bd",
      "download_url": "https://raw.githubusercontent.com/octocat/HelloWorld/master/notes/hello.txt",
      "type": "file",
      "_links": {
       "self": "https://api.github.com/repos/octocat/Hello-World/contents/notes/hello.txt",
       "git": "https://api.github.com/repos/octocat/Hello-World/git/blobs/a56507ed892d05a37c6d6128c260937ea4d287bd",
       "html": "https://github.com/octocat/Hello-World/blob/master/notes/hello.txt"
      }
     },
     "commit": {
      "sha": "18a43cd8e1e3a79c786e3d808a73d23b6d212b16",
      "node_id": "MDY6Q29tbWl0MThhNDNjZDhlMWUzYTc5Yzc4NmUzZDgwOGE3M2QyM2I2ZDIxMmIxNg==",
      "url": "https://api.github.com/repos/octocat/Hello-World/git/commits/18a43cd8e1e3a79c786e3d808a73d23b6d212b16",
      "html_url": "https://github.com/octocat/Hello-World/git/commit/18a43cd8e1e3a79c786e3d808a73d23b6d212b16",
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
       "url": "https://api.github.com/repos/octocat/Hello-World/git/trees/9a21f8e2018f42ffcf369b24d2cd20bc25c9e66f",
       "sha": "9a21f8e2018f42ffcf369b24d2cd20bc25c9e66f"
      },
      "parents": [
       {
        "url": "https://api.github.com/repos/octocat/Hello-World/git/commits/da5a433788da5c255edad7979b328b67d79f53f6",
        "html_url": "https://github.com/octocat/Hello-World/git/commit/da5a433788da5c255edad7979b328b67d79f53f6",
        "sha": "da5a433788da5c255edad7979b328b67d79f53f6"
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


