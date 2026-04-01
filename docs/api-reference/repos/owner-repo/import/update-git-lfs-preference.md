# Update Git LFS preference

You can import repositories from Subversion, Mercurial, and TFS that include files larger than 100MB. This ability is powered by [Git LFS](https://git-lfs.github.com). You can learn more about our LFS feature and working with large files [on our help site](https://help.github.com/articles/versioning-large-files/).

```http
PATCH {{baseUrl}}/repos/:owner/:repo/import/lfs
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
        "use_lfs": "<string>"
    }
    ```


## Responses


=== "200 OK"

    response

    ```json
    {
     "vcs": "subversion",
     "use_lfs": "opt_in",
     "vcs_url": "http://svn.mycompany.com/svn/myproject",
     "status": "complete",
     "status_text": "Done",
     "has_large_files": true,
     "large_files_size": 132331036,
     "large_files_count": 1,
     "authors_count": 4,
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


