# List SAML SSO authorizations for an organization

Listing and deleting credential authorizations is available to organizations with GitHub Enterprise Cloud. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products).

An authenticated organization owner with the `read:org` scope can list all credential authorizations for an organization that uses SAML single sign-on (SSO). The credentials are either personal access tokens or SSH keys that organization members have authorized for the organization. For more information, see [About authentication with SAML single sign-on](https://help.github.com/en/articles/about-authentication-with-saml-single-sign-on).

```http
GET {{baseUrl}}/orgs/:org/credential-authorizations
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `org` | `string` | `Path` | `Yes` | (Required)  |



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
      "login": "octocat",
      "credential_id": 161195,
      "credential_type": "personal access token",
      "token_last_eight": "71c3fc11",
      "credential_authorized_at": "2011-01-26T19:06:43Z",
      "scopes": [
       "user",
       "repo"
      ]
     },
     {
      "login": "hubot",
      "credential_id": 161196,
      "credential_type": "personal access token",
      "token_last_eight": "12345678",
      "credential_authorized_at": "2019-03-29T19:06:43Z",
      "scopes": [
       "repo"
      ]
     }
    ]
    ```


