# List gist forks



```http
GET {{baseUrl}}/gists/:gist_id/forks?per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `gist_id` | `string` | `Path` | `Yes` | (Required) gist_id parameter |

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
      "url": "https://api.github.com/gists/dee9c42e4998ce2ea439",
      "id": "dee9c42e4998ce2ea439",
      "created_at": "2011-04-14T16:00:49Z",
      "updated_at": "2011-04-14T16:00:49Z"
     }
    ]
    ```


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


=== "403 Forbidden"

    Forbidden

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
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


