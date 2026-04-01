# Get the last year of commit activity

Returns the last year of commit activity grouped by week. The `days` array is a group of commits per day, starting on `Sunday`.

```http
GET {{baseUrl}}/repos/:owner/:repo/stats/commit_activity
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

    response

    ```json
    [
     {
      "days": [
       0,
       3,
       26,
       20,
       39,
       1,
       0
      ],
      "total": 89,
      "week": 1336280400
     }
    ]
    ```


