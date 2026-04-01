# Get SCIM provisioning information for a user



```http
GET {{baseUrl}}/scim/v2/organizations/:org/Users/:scim_user_id
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `org` | `string` | `Path` | `Yes` | (Required)  |

| `scim_user_id` | `string` | `Path` | `Yes` | (Required) scim_user_id parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "304 Not Modified"

    Not Modified

    ```json
    
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


