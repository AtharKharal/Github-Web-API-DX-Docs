# Delete a project

Deletes a project board. Returns a `404 Not Found` status if projects are disabled.

```http
DELETE {{baseUrl}}/projects/:project_id
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `project_id` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "304 Not Modified"

    Not Modified

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


=== "401 Unauthorized"

    Requires Authentication

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "204 No Content"

    Delete Success

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


=== "410 Gone"

    Gone

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


