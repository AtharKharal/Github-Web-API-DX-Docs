# API Architecture Overview

The GitHub Web API is built on a modular, resource-oriented architecture. We prioritize:

---

## 1. Resource Hierarchy

The API organizes data into logical resources (e.g., `user`, `repo`, `org`). Each resource has a unique URI and a deterministic structure.

---

## 2. Hypermedia Navigation

The API uses **Hypermedia as the Engine of Application State (HATEOAS)** to provide links to related resources. This ensures discoverability and reduces client-side hardcoding of URLs.

```json
{
  "login": "octocat",
  "id": 1,
  "node_id": "MDQ6VXNlcjE=",
  "avatar_url": "https://github.com/images/error/octocat_happy.gif",
  "followers_url": "https://api.github.com/users/octocat/followers",
  "..." : "..."
}
```

---

## 3. Deterministic Responses

The API returns consistent status codes and response structures for all operations. This ensures predictability and simplifies client-side error handling.

| Status Code | Meaning |
| ----------- | ------- |
| `200 OK` | The request was successful. |
| `201 Created` | The resource was created. |
| `204 No Content` | The request was successful, but no content was returned. |
| `401 Unauthorized` | The request requires authentication. |
| `403 Forbidden` | The authenticated user does not have permission for the operation. |
| `404 Not Found` | The requested resource does not exist. |

---

## 4. Performance and Rate Limiting

The API supports high-concurrency requests and utilizes efficient rate-limiting to ensure stability and fair usage.

---

## Next Steps

* **[Authentication Guide](../how-to/authentication.md)**
* **[API Reference](../api-reference/overview.md)**
