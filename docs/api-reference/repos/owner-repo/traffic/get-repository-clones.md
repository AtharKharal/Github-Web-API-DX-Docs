# Get repository clones

Get the total number of clones and breakdown per day or week for the last 14 days. Timestamps are aligned to UTC midnight of the beginning of the day or week. Week begins on Monday.

```http
GET {{baseUrl}}/repos/:owner/:repo/traffic/clones?per=day
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `per` | `string` | `Query` | `No` | Must be one of: `day`, `week`. |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "403 Forbidden"

    Forbidden

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "200 OK"

    response

    ```json
    {
     "count": 173,
     "uniques": 128,
     "clones": [
      {
       "timestamp": "2016-10-10T00:00:00Z",
       "count": 2,
       "uniques": 1
      },
      {
       "timestamp": "2016-10-11T00:00:00Z",
       "count": 17,
       "uniques": 16
      },
      {
       "timestamp": "2016-10-12T00:00:00Z",
       "count": 21,
       "uniques": 15
      },
      {
       "timestamp": "2016-10-13T00:00:00Z",
       "count": 8,
       "uniques": 7
      },
      {
       "timestamp": "2016-10-14T00:00:00Z",
       "count": 5,
       "uniques": 5
      },
      {
       "timestamp": "2016-10-15T00:00:00Z",
       "count": 2,
       "uniques": 2
      },
      {
       "timestamp": "2016-10-16T00:00:00Z",
       "count": 8,
       "uniques": 7
      },
      {
       "timestamp": "2016-10-17T00:00:00Z",
       "count": 26,
       "uniques": 15
      },
      {
       "timestamp": "2016-10-18T00:00:00Z",
       "count": 19,
       "uniques": 17
      },
      {
       "timestamp": "2016-10-19T00:00:00Z",
       "count": 19,
       "uniques": 14
      },
      {
       "timestamp": "2016-10-20T00:00:00Z",
       "count": 19,
       "uniques": 15
      },
      {
       "timestamp": "2016-10-21T00:00:00Z",
       "count": 9,
       "uniques": 7
      },
      {
       "timestamp": "2016-10-22T00:00:00Z",
       "count": 5,
       "uniques": 5
      },
      {
       "timestamp": "2016-10-23T00:00:00Z",
       "count": 6,
       "uniques": 5
      },
      {
       "timestamp": "2016-10-24T00:00:00Z",
       "count": 7,
       "uniques": 5
      }
     ]
    }
    ```


