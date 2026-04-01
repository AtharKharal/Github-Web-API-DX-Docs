# List organization invitation teams

List all teams associated with an invitation. In order to see invitations in an organization, the authenticated user must be an organization owner.

```http
GET {{baseUrl}}/orgs/:org/invitations/:invitation_id/teams?per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `org` | `string` | `Path` | `Yes` | (Required)  |

| `invitation_id` | `string` | `Path` | `Yes` | (Required) invitation_id parameter |

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
      "id": 1,
      "node_id": "MDQ6VGVhbTE=",
      "url": "https://api.github.com/teams/1",
      "html_url": "https://api.github.com/teams/justice-league",
      "name": "Justice League",
      "slug": "justice-league",
      "description": "A great team.",
      "privacy": "closed",
      "permission": "admin",
      "members_url": "https://api.github.com/teams/1/members{/member}",
      "repositories_url": "https://api.github.com/teams/1/repos",
      "parent": null
     }
    ]
    ```


=== "404 Not Found"

    Resource Not Found

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


