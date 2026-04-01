# Move a project card



```http
POST {{baseUrl}}/projects/columns/cards/:card_id/moves
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `card_id` | `string` | `Path` | `Yes` | (Required) card_id parameter |



## Request Body

=== "JSON"

    ```json
    {
        "position": "<string>",
        "column_id": "<integer>"
    }
    ```


## Responses


=== "403 Forbidden"

    Forbidden

    ```json
    {
     "message": "enim culpa",
     "documentation_url": "eu consequat",
     "errors": [
      {
       "code": "anim des",
       "message": "ut do anim consequat",
       "resource": "minim Duis con",
       "field": "enim reprehenderit in"
      },
      {
       "code": "laborum aute voluptate id",
       "message": "dolore magna",
       "resource": "nulla cillum ut labore",
       "field": "et labore aliqua"
      }
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


=== "422 Unprocessable Entity (WebDAV) (RFC 4918)"

    Validation Failed

    ```json
    {
     "message": "culpa mollit",
     "documentation_url": "ipsum ut",
     "errors": [
      {
       "code": "consequat enim et velit",
       "resource": "anim ullamco",
       "field": "voluptate officia amet",
       "message": "exercitation sed dolore est",
       "index": 18359415,
       "value": "ullamco ut velit nulla eiusmod"
      },
      {
       "code": "occaecat eiusmod Duis",
       "resource": "esse ad Excepteur mollit",
       "field": "minim ipsum nisi exercitation non",
       "message": "proident reprehenderit",
       "index": -23326731,
       "value": "adipisicing cupidatat culpa in"
      }
     ]
    }
    ```


=== "503 Service Unavailable"

    Service Unavailable

    ```json
    {
     "code": "reprehenderit magna veniam in nulla",
     "message": "sit",
     "documentation_url": "qui",
     "errors": [
      {
       "code": "v",
       "message": "pariatur veniam irure occaecat"
      },
      {
       "code": "quis incididunt elit pariatur mollit",
       "message": "deserunt aliquip ut m"
      }
     ]
    }
    ```


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


