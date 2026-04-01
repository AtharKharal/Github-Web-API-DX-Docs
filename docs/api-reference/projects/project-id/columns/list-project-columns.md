# List project columns



```http
GET {{baseUrl}}/projects/:project_id/columns?per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `project_id` | `string` | `Path` | `Yes` | (Required)  |

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
      "url": "https://api.github.com/projects/columns/367",
      "project_url": "https://api.github.com/projects/120",
      "cards_url": "https://api.github.com/projects/columns/367/cards",
      "id": 367,
      "node_id": "MDEzOlByb2plY3RDb2x1bW4zNjc=",
      "name": "To Do",
      "created_at": "2016-09-05T14:18:44Z",
      "updated_at": "2016-09-05T14:22:28Z"
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


=== "403 Forbidden"

    Forbidden

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


