# List labels for issues in a milestone



```http
GET {{baseUrl}}/repos/:owner/:repo/milestones/:milestone_number/labels?per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `milestone_number` | `string` | `Path` | `Yes` | (Required) milestone_number parameter |

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
      "id": 208045946,
      "node_id": "MDU6TGFiZWwyMDgwNDU5NDY=",
      "url": "https://api.github.com/repos/octocat/Hello-World/labels/bug",
      "name": "bug",
      "description": "Something isn't working",
      "color": "f29513",
      "default": true
     },
     {
      "id": 208045947,
      "node_id": "MDU6TGFiZWwyMDgwNDU5NDc=",
      "url": "https://api.github.com/repos/octocat/Hello-World/labels/enhancement",
      "name": "enhancement",
      "description": "New feature or request",
      "color": "a2eeef",
      "default": false
     }
    ]
    ```


