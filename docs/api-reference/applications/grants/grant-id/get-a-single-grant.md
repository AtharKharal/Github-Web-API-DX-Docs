# Get a single grant

**Deprecation Notice:** GitHub will discontinue the [OAuth Authorizations API](https://developer.github.com/v3/oauth_authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow). The [OAuth Authorizations API](https://developer.github.com/v3/oauth_authorizations/) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).

```http
GET {{baseUrl}}/applications/grants/:grant_id
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `grant_id` | `string` | `Path` | `Yes` | (Required) grant_id parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "403 Forbidden"

    Forbidden

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


=== "401 Unauthorized"

    Requires Authentication

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "200 OK"

    response

    ```json
    {
     "id": 1,
     "url": "https://api.github.com/applications/grants/1",
     "app": {
      "url": "http://my-github-app.com",
      "name": "my github app",
      "client_id": "abcde12345fghij67890"
     },
     "created_at": "2011-09-06T17:26:27Z",
     "updated_at": "2011-09-06T20:39:23Z",
     "scopes": [
      "public_repo"
     ]
    }
    ```


