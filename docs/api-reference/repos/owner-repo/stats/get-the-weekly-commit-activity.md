# Get the weekly commit activity

Returns a weekly aggregate of the number of additions and deletions pushed to a repository.

```http
GET {{baseUrl}}/repos/:owner/:repo/stats/code_frequency
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "200 OK"

    Returns a weekly aggregate of the number of additions and deletions pushed to a repository.

    ```json
    [
     [
      1302998400,
      1124,
      -435
     ]
    ]
    ```


