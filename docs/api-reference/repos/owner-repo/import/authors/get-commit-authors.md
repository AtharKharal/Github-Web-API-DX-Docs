# Get commit authors

Each type of source control system represents authors in a different way. For example, a Git commit author has a display name and an email address, but a Subversion commit author just has a username. The GitHub Importer will make the author information valid, but the author might not be correct. For example, it will change the bare Subversion username `hubot` into something like `hubot <hubot@12341234-abab-fefe-8787-fedcba987654>`.

This endpoint and the [Map a commit author](https://developer.github.com/v3/migrations/source_imports/#map-a-commit-author) endpoint allow you to provide correct Git author information.

```http
GET {{baseUrl}}/repos/:owner/:repo/import/authors?since=<string>
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `since` | `string` | `Query` | `No` | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. |



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
    [
     {
      "id": 2268557,
      "remote_id": "nobody@fc7da526-431c-80fe-3c8c-c148ff18d7ef",
      "remote_name": "nobody",
      "email": "hubot@github.com",
      "name": "Hubot",
      "url": "https://api.github.com/repos/octocat/socm/import/authors/2268557",
      "import_url": "https://api.github.com/repos/octocat/socm/import"
     },
     {
      "id": 2268558,
      "remote_id": "svner@fc7da526-431c-80fe-3c8c-c148ff18d7ef",
      "remote_name": "svner",
      "email": "svner@fc7da526-431c-80fe-3c8c-c148ff18d7ef",
      "name": "svner",
      "url": "https://api.github.com/repos/octocat/socm/import/authors/2268558",
      "import_url": "https://api.github.com/repos/octocat/socm/import"
     },
     {
      "id": 2268559,
      "remote_id": "svner@example.com@fc7da526-431c-80fe-3c8c-c148ff18d7ef",
      "remote_name": "svner@example.com",
      "email": "svner@example.com@fc7da526-431c-80fe-3c8c-c148ff18d7ef",
      "name": "svner@example.com",
      "url": "https://api.github.com/repos/octocat/socm/import/authors/2268559",
      "import_url": "https://api.github.com/repos/octocat/socm/import"
     }
    ]
    ```


