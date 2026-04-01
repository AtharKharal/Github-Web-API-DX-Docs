# Remove all labels from an issue



```http
DELETE {{baseUrl}}/repos/:owner/:repo/issues/:issue_number/labels
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `issue_number` | `string` | `Path` | `Yes` | (Required) issue_number parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "410 Gone"

    Gone

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


