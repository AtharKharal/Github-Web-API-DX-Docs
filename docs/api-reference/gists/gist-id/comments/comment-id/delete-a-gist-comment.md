# Delete a gist comment



```http
DELETE {{baseUrl}}/gists/:gist_id/comments/:comment_id
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `gist_id` | `string` | `Path` | `Yes` | (Required) gist_id parameter |

| `comment_id` | `string` | `Path` | `Yes` | (Required) comment_id parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


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


=== "204 No Content"

    Empty response

    ```json
    
    ```


=== "404 Not Found"

    Resource Not Found

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


