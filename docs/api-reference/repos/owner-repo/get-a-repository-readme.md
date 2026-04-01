# Get a repository README

Gets the preferred README for a repository.

READMEs support [custom media types](https://developer.github.com/v3/repos/contents/#custom-media-types) for retrieving the raw content or rendered HTML.

```http
GET {{baseUrl}}/repos/:owner/:repo/readme?ref=<string>
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `ref` | `string` | `Query` | `No` | The name of the commit/branch/tag. Default: the repository’s default branch (usually `master`) |



## Request Body

=== "JSON"

    ```json
    
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


=== "200 OK"

    response

    ```json
    {
     "type": "file",
     "encoding": "base64",
     "size": 5362,
     "name": "README.md",
     "path": "README.md",
     "content": "encoded content ...",
     "sha": "3d21ec53a331a6f037a91c368710b99387d012c1",
     "url": "https://api.github.com/repos/octokit/octokit.rb/contents/README.md",
     "git_url": "https://api.github.com/repos/octokit/octokit.rb/git/blobs/3d21ec53a331a6f037a91c368710b99387d012c1",
     "html_url": "https://github.com/octokit/octokit.rb/blob/master/README.md",
     "download_url": "https://raw.githubusercontent.com/octokit/octokit.rb/master/README.md",
     "_links": {
      "git": "https://api.github.com/repos/octokit/octokit.rb/git/blobs/3d21ec53a331a6f037a91c368710b99387d012c1",
      "self": "https://api.github.com/repos/octokit/octokit.rb/contents/README.md",
      "html": "https://github.com/octokit/octokit.rb/blob/master/README.md"
     }
    }
    ```


