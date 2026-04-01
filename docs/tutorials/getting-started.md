# Getting Started with the GitHub API

This tutorial provides a step-by-step guide to making your first successful request to the GitHub Web API.

---

## 1. Prerequisites

Before you begin, ensure you have the following:

* A **GitHub Account**.
* A **Terminal** (e.g., PowerShell, Bash).
* **cURL** or a similar HTTP client installed.

---

## 2. Authentication

The GitHub API requires authentication for most operations. For this tutorial, we will use a **Personal Access Token (PAT)**.

1. Navigate to **Settings > Developer settings > Personal access tokens**.
2. Click **Generate new token**.
3. Select the `repo` and `user` scopes.
4. Copy the token and store it securely.

!!! warning "Token Security"
    Never commit your personal access token to version control. Use environment variables to manage credentials.

---

## 3. Your First API Call

Open your terminal and run the following command to fetch your user profile:

```bash
curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/user
```

### Understanding the Response

A successful request returns a JSON object containing your profile information:

```json
{
  "login": "octocat",
  "id": 1,
  "node_id": "MDQ6VXNlcjE=",
  "avatar_url": "https://github.com/images/error/octocat_happy.gif",
  "..." : "..."
}
```

---

## Next Steps

Now that you've made your first call, explore the following resources:

* **[Authentication Deep-Dive](../how-to/authentication.md)**
* **[API Reference](../api-reference/overview.md)**
