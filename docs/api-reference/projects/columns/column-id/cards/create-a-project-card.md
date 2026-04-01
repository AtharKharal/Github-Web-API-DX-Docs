# Create a project card

**Note**: GitHub's REST API v3 considers every pull request an issue, but not every issue is a pull request. For this reason, "Issues" endpoints may return both issues and pull requests in the response. You can identify pull requests by the `pull_request` key.

Be aware that the `id` of a pull request returned from "Issues" endpoints will be an _issue id_. To find out the pull request id, use the "[List pull requests](https://developer.github.com/v3/pulls/#list-pull-requests)" endpoint.

```http
POST {{baseUrl}}/projects/columns/:column_id/cards
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `column_id` | `string` | `Path` | `Yes` | (Required) column_id parameter |



## Request Body

=== "JSON"

    ```json
    {
        "note": "<string>"
    }
    ```


## Responses


=== "201 Created"

    response

    ```json
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
    ```


=== "401 Unauthorized"

    Requires Authentication

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


=== "503 Service Unavailable"

    Service Unavailable

    ```json
    {
     "code": "reprehenderit magna veniam in nulla",
     "message": "sit",
     "documentation_url": "qui",
     "errors": [
      {
       "code": "v",
       "message": "pariatur veniam irure occaecat"
      },
      {
       "code": "quis incididunt elit pariatur mollit",
       "message": "deserunt aliquip ut m"
      }
     ]
    }
    ```


=== "403 Forbidden"

    Forbidden

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


