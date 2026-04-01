# Update an import

An import can be updated with credentials or a project choice by passing in the appropriate parameters in this API
request. If no parameters are provided, the import will be restarted.

```http
PATCH {{baseUrl}}/repos/:owner/:repo/import
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
        "vcs_username": "<string>",
        "vcs_password": "<string>",
        "vcs": "<string>",
        "tfvc_project": "<string>"
    }
    ```


## Responses


=== "200 OK"

    response

    ```json
    {
     "vcs": "subversion",
     "use_lfs": "undecided",
     "vcs_url": "http://svn.mycompany.com/svn/myproject",
     "status": "detecting",
     "url": "https://api.github.com/repos/octocat/socm/import",
     "html_url": "https://import.github.com/octocat/socm/import",
     "authors_url": "https://api.github.com/repos/octocat/socm/import/authors",
     "repository_url": "https://api.github.com/repos/octocat/socm"
    }
    ```


