# Map a commit author

Update an author's identity for the import. Your application can continue updating authors any time before you push new commits to the repository.

```http
PATCH {{baseUrl}}/repos/:owner/:repo/import/authors/:author_id
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `author_id` | `string` | `Path` | `Yes` | (Required) author_id parameter |



## Request Body

=== "JSON"

    ```json
    {
        "email": "<string>",
        "name": "<string>",
        "remote_id": "<string>"
    }
    ```


## Responses


=== "200 OK"

    response

    ```json
    {
     "id": 2268557,
     "remote_id": "nobody@fc7da526-431c-80fe-3c8c-c148ff18d7ef",
     "remote_name": "nobody",
     "email": "hubot@github.com",
     "name": "Hubot",
     "url": "https://api.github.com/repos/octocat/socm/import/authors/2268557",
     "import_url": "https://api.github.com/repos/octocat/socm/import"
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


