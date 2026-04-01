# Get a code scanning alert

Gets a single code scanning alert. You must use an access token with the `security_events` scope to use this endpoint. GitHub Apps must have the `security_events` read permission to use this endpoint.

The security `alert_id` is found at the end of the security alert's URL. For example, the security alert ID for `https://github.com/Octo-org/octo-repo/security/code-scanning/88` is `88`.

```http
GET {{baseUrl}}/repos/:owner/:repo/code-scanning/alerts/:alert_id
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `alert_id` | `string` | `Path` | `Yes` | (Required) alert_id parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "503 Service Unavailable"

    Service Unavailable

    ```json
    {
     "code": "nisi",
     "message": "enim amet nostrud",
     "documentation_url": "reprehenderit id"
    }
    ```


=== "404 Not Found"

    Resource Not Found

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
     "rule_id": "js/useless-expression",
     "rule_severity": "warning",
     "rule_description": "Expression has no effect",
     "tool": "CodeQL",
     "created_at": "2020-05-06T12:00:00Z",
     "open": true,
     "closed_by": null,
     "closed_at": null,
     "url": "https://api.github.com/repos/Octo-org/octo-repo/code-scanning/alerts/88",
     "html_url": "https://github.com/Octo-org/octo-repo/security/code-scanning/88"
    }
    ```


