# Get top referral sources

Get the top 10 referrers over the last 14 days.

```http
GET {{baseUrl}}/repos/:owner/:repo/traffic/popular/referrers
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
      "referrer": "Google",
      "count": 4,
      "uniques": 3
     },
     {
      "referrer": "stackoverflow.com",
      "count": 2,
      "uniques": 2
     },
     {
      "referrer": "eggsonbread.com",
      "count": 1,
      "uniques": 1
     },
     {
      "referrer": "yandex.ru",
      "count": 1,
      "uniques": 1
     }
    ]
    ```


=== "403 Forbidden"

    Forbidden

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


