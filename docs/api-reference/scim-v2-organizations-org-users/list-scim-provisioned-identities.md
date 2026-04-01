# List SCIM provisioned identities

Retrieves a paginated list of all provisioned organization members, including pending invitations. If you provide the `filter` parameter, the resources for all matching provisions members are returned.

When a user with a SAML-provisioned external identity leaves (or is removed from) an organization, the account's metadata is immediately removed. However, the returned list of user accounts might not always match the organization or enterprise member list you see on GitHub. This can happen in certain cases where an external identity associated with an organization will not match an organization member:
  - When a user with a SCIM-provisioned external identity is removed from an organization, the account's metadata is preserved to allow the user to re-join the organization in the future.
  - When inviting a user to join an organization, you can expect to see their external identity in the results before they accept the invitation, or if the invitation is cancelled (or never accepted).
  - When a user is invited over SCIM, an external identity is created that matches with the invitee's email address. However, this identity is only linked to a user account when the user accepts the invitation by going through SAML SSO.

The returned list of external identities can include an entry for a `null` user. These are unlinked SAML identities that are created when a user goes through the following Single Sign-On (SSO) process but does not sign in to their GitHub account after completing SSO:

1. The user is granted access by the IdP and is not a member of the GitHub organization.

1. The user attempts to access the GitHub organization and initiates the SAML SSO process, and is not currently signed in to their GitHub account.

1. After successfully authenticating with the SAML SSO IdP, the `null` external identity entry is created and the user is prompted to sign in to their GitHub account:
   - If the user signs in, their GitHub account is linked to this entry.
   - If the user does not sign in (or does not create a new account when prompted), they are not added to the GitHub organization, and the external identity `null` entry remains in place.

```http
GET {{baseUrl}}/scim/v2/organizations/:org/Users?startIndex=<integer>&count=<integer>&filter=<string>
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `org` | `string` | `Path` | `Yes` | (Required)  |

| `startIndex` | `string` | `Query` | `No` | Used for pagination: the index of the first result to return. |

| `count` | `string` | `Query` | `No` | Used for pagination: the number of results to return. |

| `filter` | `string` | `Query` | `No` | Filters results using the equals query parameter operator (`eq`). You can filter results that are equal to `id`, `userName`, `emails`, and `external_id`. For example, to search for an identity with the `userName` Octocat, you would use this query:

`?filter=userName%20eq%20\"Octocat\"`.

To filter results for for the identity with the email `octocat@github.com`, you would use this query:

`?filter=emails%20eq%20\"octocat@github.com\"`. |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "200 OK"

    response

    ```json
    {
     "schemas": [
      "urn:ietf:params:scim:api:messages:2.0:ListResponse"
     ],
     "totalResults": 1,
     "itemsPerPage": 1,
     "startIndex": 1,
     "Resources": [
      {
       "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User"
       ],
       "id": "5fc0c238-1112-11e8-8e45-920c87bdbd75",
       "externalId": "00u1dhhb1fkIGP7RL1d8",
       "userName": "octocat@github.com",
       "displayName": "Mona Octocat",
       "name": {
        "givenName": "Mona",
        "familyName": "Octocat",
        "formatted": "Mona Octocat"
       },
       "emails": [
        {
         "value": "octocat@github.com",
         "primary": true
        }
       ],
       "active": true,
       "meta": {
        "resourceType": "User",
        "created": "2018-02-13T15:05:24.000-08:00",
        "lastModified": "2018-02-13T15:05:55.000-08:00",
        "location": "https://api.github.com/scim/v2/organizations/octo-org/Users/5fc0c238-1112-11e8-8e45-920c87bdbd75"
       }
      }
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
     "message": "cillum est consequat fugiat quis",
     "documentation_url": "deserunt quis",
     "detail": "anim cupidatat cillum incididunt",
     "status": -38038469,
     "scimType": "in Lorem id voluptate",
     "schemas": [
      "nulla anim",
      "id est ea"
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


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


