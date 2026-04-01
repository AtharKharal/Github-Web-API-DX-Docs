# Delete a project card



```http
DELETE {{baseUrl}}/projects/columns/cards/:card_id
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `card_id` | `string` | `Path` | `Yes` | (Required) card_id parameter |



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


=== "204 No Content"

    Empty response

    ```json
    
    ```


=== "403 Forbidden"

    Forbidden

    ```json
    {
     "message": "elit",
     "documentation_url": "nostrud laboris enim",
     "errors": [
      "occaecat irure et dolore",
      "aute Duis"
     ]
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


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


