# Move a project column



```http
POST {{baseUrl}}/projects/columns/:column_id/moves
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `column_id` | `string` | `Path` | `Yes` | (Required) column_id parameter |



## Request Body

=== "JSON"

    ```json
    {
        "position": "<string>"
    }
    ```


## Responses


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


=== "401 Unauthorized"

    Requires Authentication

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "201 Created"

    response

    ```json
    {}
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


