# Delete a deploy key

Deploy keys are immutable. If you need to update a key, remove the key and create a new one instead.

```http
DELETE {{baseUrl}}/repos/:owner/:repo/keys/:key_id
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `key_id` | `string` | `Path` | `Yes` | (Required) key_id parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "204 No Content"

    Empty response

    ```json
    
    ```


