# Start an import

Start a source import to a GitHub repository using GitHub Importer.

```http
PUT {{baseUrl}}/repos/:owner/:repo/import
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
        "vcs_url": "<string>",
        "vcs": "<string>",
        "vcs_username": "<string>",
        "vcs_password": "<string>",
        "tfvc_project": "<string>"
    }
    ```


## Responses


=== "201 Created"

    response

    ```json
    {
     "vcs": "subversion",
     "use_lfs": "undecided",
     "vcs_url": "http://svn.mycompany.com/svn/myproject",
     "status": "importing",
     "status_text": "Importing...",
     "has_large_files": false,
     "large_files_size": 0,
     "large_files_count": 0,
     "authors_count": 0,
     "commit_count": 1042,
     "url": "https://api.github.com/repos/octocat/socm/import",
     "html_url": "https://import.github.com/octocat/socm/import",
     "authors_url": "https://api.github.com/repos/octocat/socm/import/authors",
     "repository_url": "https://api.github.com/repos/octocat/socm"
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


