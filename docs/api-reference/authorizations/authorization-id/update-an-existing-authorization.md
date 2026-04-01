# Update an existing authorization

**Deprecation Notice:** GitHub will discontinue the [OAuth Authorizations API](https://developer.github.com/v3/oauth_authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow). The [OAuth Authorizations API](https://developer.github.com/v3/oauth_authorizations/) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).

If you have two-factor authentication setup, Basic Authentication for this endpoint requires that you use a one-time password (OTP) and your username and password instead of tokens. For more information, see "[Working with two-factor authentication](https://developer.github.com/v3/auth/#working-with-two-factor-authentication)."

You can only send one of these scope keys at a time.

```http
PATCH {{baseUrl}}/authorizations/:authorization_id
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `authorization_id` | `string` | `Path` | `Yes` | (Required) authorization_id parameter |



## Request Body

=== "JSON"

    ```json
    {
        "scopes": [
            "<string>",
            "<string>"
        ],
        "add_scopes": [
            "<string>",
            "<string>"
        ],
        "remove_scopes": [
            "<string>",
            "<string>"
        ],
        "note": "<string>",
        "note_url": "<string>",
        "fingerprint": "<string>"
    }
    ```


## Responses


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


=== "200 OK"

    response

    ```json
    {
     "id": 1,
     "url": "https://api.github.com/authorizations/1",
     "scopes": [
      "public_repo"
     ],
     "token": "",
     "token_last_eight": "12345678",
     "hashed_token": "25f94a2a5c7fbaf499c665bc73d67c1c87e496da8985131633ee0a95819db2e8",
     "app": {
      "url": "http://my-github-app.com",
      "name": "my github app",
      "client_id": "abcde12345fghij67890"
     },
     "note": "optional note",
     "note_url": "http://optional/note/url",
     "updated_at": "2011-09-06T20:39:23Z",
     "created_at": "2011-09-06T17:26:27Z",
     "fingerprint": "jklmnop12345678"
    }
    ```


