# Create a project column



```http
POST {{baseUrl}}/projects/:project_id/columns
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `project_id` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    {
        "name": "<string>"
    }
    ```


## Responses


=== "304 Not Modified"

    Not Modified

    ```json
    
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


=== "201 Created"

    response

    ```json
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
    ```


=== "403 Forbidden"

    Forbidden

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


