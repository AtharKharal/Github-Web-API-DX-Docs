# Create a GitHub App from a manifest

Use this endpoint to complete the handshake necessary when implementing the [GitHub App Manifest flow](https://developer.github.com/apps/building-github-apps/creating-github-apps-from-a-manifest/). When you create a GitHub App with the manifest flow, you receive a temporary `code` used to retrieve the GitHub App's `id`, `pem` (private key), and `webhook_secret`.

```http
POST {{baseUrl}}/app-manifests/:code/conversions
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `code` | `string` | `Path` | `Yes` | (Required) code parameter |



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


=== "422 Unprocessable Entity (WebDAV) (RFC 4918)"

    Validation Failed

    ```json
    {
     "message": "exercitation incididunt ut et",
     "documentation_url": "v",
     "errors": [
      "Duis incididunt dolor culpa",
      "voluptate Lorem"
     ]
    }
    ```


=== "201 Created"

    response

    ```json
    {
     "id": 1,
     "slug": "octoapp",
     "node_id": "MDxOkludGVncmF0aW9uMQ==",
     "owner": {
      "login": "github",
      "id": 1,
      "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
      "url": "https://api.github.com/orgs/github",
      "repos_url": "https://api.github.com/orgs/github/repos",
      "events_url": "https://api.github.com/orgs/github/events",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": true
     },
     "name": "Octocat App",
     "description": "",
     "external_url": "https://example.com",
     "html_url": "https://github.com/apps/octoapp",
     "created_at": "2017-07-08T16:18:44-04:00",
     "updated_at": "2017-07-08T16:18:44-04:00",
     "permissions": {
      "metadata": "read",
      "contents": "read",
      "issues": "write",
      "single_file": "write"
     },
     "events": [
      "push",
      "pull_request"
     ],
     "client_id": "Iv1.8a61f9b3a7aba766",
     "client_secret": "1726be1638095a19edd134c77bde3aa2ece1e5d8",
     "webhook_secret": "e340154128314309424b7c8e90325147d99fdafa",
     "pem": "{{vault:rsa-private-key}}\n"
    }
    ```


