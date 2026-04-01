# Get page views

Get the total number of views and breakdown per day or week for the last 14 days. Timestamps are aligned to UTC midnight of the beginning of the day or week. Week begins on Monday.

```http
GET {{baseUrl}}/repos/:owner/:repo/traffic/views?per=day
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


=== "200 OK"

    response

    ```json
    {
     "count": 14850,
     "uniques": 3782,
     "views": [
      {
       "timestamp": "2016-10-10T00:00:00Z",
       "count": 440,
       "uniques": 143
      },
      {
       "timestamp": "2016-10-11T00:00:00Z",
       "count": 1308,
       "uniques": 414
      },
      {
       "timestamp": "2016-10-12T00:00:00Z",
       "count": 1486,
       "uniques": 452
      },
      {
       "timestamp": "2016-10-13T00:00:00Z",
       "count": 1170,
       "uniques": 401
      },
      {
       "timestamp": "2016-10-14T00:00:00Z",
       "count": 868,
       "uniques": 266
      },
      {
       "timestamp": "2016-10-15T00:00:00Z",
       "count": 495,
       "uniques": 157
      },
      {
       "timestamp": "2016-10-16T00:00:00Z",
       "count": 524,
       "uniques": 175
      },
      {
       "timestamp": "2016-10-17T00:00:00Z",
       "count": 1263,
       "uniques": 412
      },
      {
       "timestamp": "2016-10-18T00:00:00Z",
       "count": 1402,
       "uniques": 417
      },
      {
       "timestamp": "2016-10-19T00:00:00Z",
       "count": 1394,
       "uniques": 424
      },
      {
       "timestamp": "2016-10-20T00:00:00Z",
       "count": 1492,
       "uniques": 448
      },
      {
       "timestamp": "2016-10-21T00:00:00Z",
       "count": 1153,
       "uniques": 332
      },
      {
       "timestamp": "2016-10-22T00:00:00Z",
       "count": 566,
       "uniques": 168
      },
      {
       "timestamp": "2016-10-23T00:00:00Z",
       "count": 675,
       "uniques": 184
      },
      {
       "timestamp": "2016-10-24T00:00:00Z",
       "count": 614,
       "uniques": 237
      }
     ]
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


