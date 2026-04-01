# Authentication Mechanisms

The GitHub API supports several authentication mechanisms. Choose the one that best fits your integration's architectural requirements.

---

## 1. Personal Access Tokens (PAT)

* **Best for**: Scripting, local testing, and command-line tools.

1. Navigate to **Settings > Developer settings > Personal access tokens**.
2. Generate a new token with the desired scopes.
3. Include the token in the `Authorization` header.

```http
Authorization: token YOUR_TOKEN_HERE
```

---

## 2. OAuth Apps

**Best for**: Third-party applications that need to access a user's GitHub data on their behalf.

1. Register your application.
2. Request authorization from the user.
3. Exchange the authorization code for an access token.

---

## 3. GitHub Apps

**Best for**: Complex integrations that need to act on behalf of an organization or repository.

1. Register a GitHub App.
2. Install the app on a target account.
3. Use a **JSON Web Token (JWT)** to authenticate as the app.
4. Exchange the JWT for an installation access token.

!!! important "Best Practice"
    GitHub Apps are the recommended way to integrate with GitHub, providing finer-grained permissions and improved security.

---

## 4. Troubleshooting Authentication

If you receive a `401 Unauthorized` response:

* **Check Token Scopes**: Ensure your token has the necessary permissions for the endpoint.
* **Token Expiration**: Verify that your token has not expired.
* **Header Format**: Ensure the `Authorization` header is formatted correctly.

---

## Next Steps

* **[API Reference](../api-reference/overview.md)**
* **[Architecture Overview](../explanation/architecture.md)**
