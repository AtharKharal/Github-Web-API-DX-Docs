# Provision and invite a SCIM user

Provision organization membership for a user, and send an activation email to the email address.

```http
POST {{baseUrl}}/scim/v2/organizations/:org/Users
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `org` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    {
        "userName": "<string>",
        "name": {
            "givenName": "<string>",
            "familyName": "<string>",
            "formatted": "<string>"
        },
        "emails": [
            {
                "value": "<string>",
                "primary": "<boolean>",
                "type": "<string>"
            }
        ],
        "displayName": "<string>",
        "schemas": [
            "<string>",
            "<string>"
        ],
        "externalId": "<string>",
        "groups": [
            "<string>",
            "<string>"
        ],
        "active": "<boolean>"
    }
    ```


## Responses


=== "500 Internal Server Error"

    Internal Error

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


=== "201 Created"

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


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


=== "409 Conflict"

    Conflict

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


