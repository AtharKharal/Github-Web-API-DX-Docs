# List project cards



```http
GET {{baseUrl}}/projects/columns/:column_id/cards?archived_state=not_archived&per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `column_id` | `string` | `Path` | `Yes` | (Required) column_id parameter |

| `archived_state` | `string` | `Query` | `No` | Filters the project cards that are returned by the card's state. Can be one of `all`,`archived`, or `not_archived`. |

| `per_page` | `string` | `Query` | `No` | Results per page (max 100) |

| `page` | `string` | `Query` | `No` | Page number of the results to fetch. |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "403 Forbidden"

    Forbidden

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
      "url": "https://api.github.com/projects/columns/cards/1478",
      "id": 1478,
      "node_id": "MDExOlByb2plY3RDYXJkMTQ3OA==",
      "note": "Add payload for delete Project column",
      "creator": {
       "login": "octocat",
       "id": 1,
       "node_id": "MDQ6VXNlcjE=",
       "avatar_url": "https://github.com/images/error/octocat_happy.gif",
       "gravatar_id": "",
       "url": "https://api.github.com/users/octocat",
       "html_url": "https://github.com/octocat",
       "followers_url": "https://api.github.com/users/octocat/followers",
       "following_url": "https://api.github.com/users/octocat/following{/other_user}",
       "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
       "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
       "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
       "organizations_url": "https://api.github.com/users/octocat/orgs",
       "repos_url": "https://api.github.com/users/octocat/repos",
       "events_url": "https://api.github.com/users/octocat/events{/privacy}",
       "received_events_url": "https://api.github.com/users/octocat/received_events",
       "type": "User",
       "site_admin": false
      },
      "created_at": "2016-09-05T14:21:06Z",
      "updated_at": "2016-09-05T14:20:22Z",
      "archived": false,
      "column_url": "https://api.github.com/projects/columns/367",
      "content_url": "https://api.github.com/repos/api-playground/projects-test/issues/3",
      "project_url": "https://api.github.com/projects/120"
     }
    ]
    ```


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


=== "401 Unauthorized"

    Requires Authentication

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


