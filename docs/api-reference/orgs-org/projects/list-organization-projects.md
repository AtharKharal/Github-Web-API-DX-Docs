# List organization projects

Lists the projects in an organization. Returns a `404 Not Found` status if projects are disabled in the organization. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned.

```http
GET {{baseUrl}}/orgs/:org/projects?state=open&per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `org` | `string` | `Path` | `Yes` | (Required)  |

| `state` | `string` | `Query` | `No` | Indicates the state of the projects to return. Can be either `open`, `closed`, or `all`. |

| `per_page` | `string` | `Query` | `No` | Results per page (max 100) |

| `page` | `string` | `Query` | `No` | Page number of the results to fetch. |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "200 OK"

    response

    ```json
    [
     {
      "owner_url": "https://api.github.com/orgs/octocat",
      "url": "https://api.github.com/projects/1002605",
      "html_url": "https://github.com/orgs/api-playground/projects/1",
      "columns_url": "https://api.github.com/projects/1002605/columns",
      "id": 1002605,
      "node_id": "MDc6UHJvamVjdDEwMDI2MDU=",
      "name": "Organization Roadmap",
      "body": "High-level roadmap for the upcoming year.",
      "number": 1,
      "state": "open",
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
      "created_at": "2011-04-11T20:09:31Z",
      "updated_at": "2014-03-04T18:58:10Z"
     }
    ]
    ```


=== "422 Unprocessable Entity (WebDAV) (RFC 4918)"

    Validation Failed

    ```json
    {
     "message": "in labore deserunt nostrud amet",
     "documentation_url": "Duis",
     "errors": [
      "nisi dolore Ut",
      "est culpa ullamco voluptate"
     ]
    }
    ```


