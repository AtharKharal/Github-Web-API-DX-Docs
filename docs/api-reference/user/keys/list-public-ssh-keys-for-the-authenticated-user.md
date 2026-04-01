# List public SSH keys for the authenticated user

Lists the public SSH keys for the authenticated user's GitHub account. Requires that you are authenticated via Basic Auth or via OAuth with at least `read:public_key` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

```http
GET {{baseUrl}}/user/keys?per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `per_page` | `string` | `Query` | `No` | Results per page (max 100) |

| `page` | `string` | `Query` | `No` | Page number of the results to fetch. |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "404 Not Found"

    Resource Not Found

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
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


=== "401 Unauthorized"

    Requires Authentication

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


=== "200 OK"

    response

    ```json
    [
     {
      "key_id": "012345678912345678",
      "key": "2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJyvv1234",
      "id": 2,
      "url": "https://api.github.com/user/keys/2",
      "title": "ssh-rsa AAAAB3NzaC1yc2EAAA",
      "created_at": "2020-06-11T21:31:57Z",
      "verified": false,
      "read_only": false
     },
     {
      "key_id": "012345678912345608",
      "key": "2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJy931234",
      "id": 3,
      "url": "https://api.github.com/user/keys/3",
      "title": "ssh-rsa AAAAB3NzaC1yc2EAAB",
      "created_at": "2020-07-11T21:31:57Z",
      "verified": false,
      "read_only": false
     }
    ]
    ```


