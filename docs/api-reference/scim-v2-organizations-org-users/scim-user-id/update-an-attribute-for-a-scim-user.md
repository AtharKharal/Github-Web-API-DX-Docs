# Update an attribute for a SCIM user

Allows you to change a provisioned user's individual attributes. To change a user's values, you must provide a specific `Operations` JSON format that contains at least one of the `add`, `remove`, or `replace` operations. For examples and more information on the SCIM operations format, see the [SCIM specification](https://tools.ietf.org/html/rfc7644#section-3.5.2).

**Note:** Complicated SCIM `path` selectors that include filters are not supported. For example, a `path` selector defined as `"path": "emails[type eq \"work\"]"` will not work.

**Warning:** If you set `active:false` using the `replace` operation (as shown in the JSON example below), it removes the user from the organization, deletes the external identity, and deletes the associated `:scim_user_id`.

```
{
  "Operations":[{
    "op":"replace",
    "value":{
      "active":false
    }
  }]
}
```

```http
PATCH {{baseUrl}}/scim/v2/organizations/:org/Users/:scim_user_id
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `org` | `string` | `Path` | `Yes` | (Required)  |

| `scim_user_id` | `string` | `Path` | `Yes` | (Required) scim_user_id parameter |



## Request Body

=== "JSON"

    ```json
    {
        "Operations": [
            {
                "op": "<string>",
                "path": "<string>",
                "value": {
                    "active": "<boolean>",
                    "userName": "<string>",
                    "externalId": "<string>",
                    "givenName": "<string>",
                    "familyName": "<string>"
                }
            }
        ],
        "schemas": [
            "<string>",
            "<string>"
        ]
    }
    ```


## Responses


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


=== "403 Forbidden"

    Forbidden

    ```json
    {
     "message": "in laborum sit ad dolor",
     "documentation_url": "Excepteur dolor",
     "detail": "Excepteur dolor aliqua ipsum",
     "status": -87592654,
     "scimType": "dolore ut",
     "schemas": [
      "exercitation",
      "occaecat aliqua consequat esse"
     ]
    }
    ```


=== "404 Not Found"

    Resource Not Found

    ```json
    {
     "message": "in laborum sit ad dolor",
     "documentation_url": "Excepteur dolor",
     "detail": "Excepteur dolor aliqua ipsum",
     "status": -87592654,
     "scimType": "dolore ut",
     "schemas": [
      "exercitation",
      "occaecat aliqua consequat esse"
     ]
    }
    ```


=== "200 OK"

    response

    ```json
    {
     "schemas": [
      "urn:ietf:params:scim:schemas:core:2.0:User"
     ],
     "id": "edefdfedf-050c-11e7-8d32",
     "externalId": "a7d0f98382",
     "userName": "mona.octocat@okta.example.com",
     "displayName": "Monalisa Octocat",
     "name": {
      "givenName": "Monalisa",
      "familyName": "Octocat",
      "formatted": "Monalisa Octocat"
     },
     "emails": [
      {
       "value": "mona.octocat@okta.example.com",
       "primary": true
      },
      {
       "value": "monalisa@octocat.github.com"
      }
     ],
     "active": true,
     "meta": {
      "resourceType": "User",
      "created": "2017-03-09T16:11:13-05:00",
      "lastModified": "2017-03-09T16:11:13-05:00",
      "location": "https://api.github.com/scim/v2/organizations/octo-org/Users/edefdfedf-050c-11e7-8d32"
     }
    }
    ```


=== "429 Too Many Requests"

    Too many requests

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "400 Bad Request"

    Bad Request

    ```json
    {
     "message": "in laborum sit ad dolor",
     "documentation_url": "Excepteur dolor",
     "detail": "Excepteur dolor aliqua ipsum",
     "status": -87592654,
     "scimType": "dolore ut",
     "schemas": [
      "exercitation",
      "occaecat aliqua consequat esse"
     ]
    }
    ```


