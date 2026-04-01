# Check if a pull request has been merged



```http
GET {{baseUrl}}/repos/:owner/:repo/pulls/:pull_number/merge
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `pull_number` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "404 Not Found"

    Response if pull request has not been merged

    ```json
    
    ```


=== "204 No Content"

    Response if pull request has been merged

    ```json
    
    ```


