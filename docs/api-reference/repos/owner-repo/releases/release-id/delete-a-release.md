# Delete a release

Users with push access to the repository can delete a release.

```http
DELETE {{baseUrl}}/repos/:owner/:repo/releases/:release_id
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `release_id` | `string` | `Path` | `Yes` | (Required) release_id parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "204 No Content"

    Empty response

    ```json
    
    ```


