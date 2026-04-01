# List public keys for a user

Lists the _verified_ public SSH keys for a user. This is accessible by anyone.

```http
GET {{baseUrl}}/users/:username/keys?per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `username` | `string` | `Path` | `Yes` | (Required)  |

| `per_page` | `string` | `Query` | `No` | Results per page (max 100) |

| `page` | `string` | `Query` | `No` | Page number of the results to fetch. |



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
      "id": 1,
      "key": "ssh-rsa AAA..."
     }
    ]
    ```


