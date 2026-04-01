# List code scanning alerts for a repository

Lists all open code scanning alerts for the default branch (usually `master`) and protected branches in a repository. You must use an access token with the `security_events` scope to use this endpoint. GitHub Apps must have the `security_events` read permission to use this endpoint.

```http
GET {{baseUrl}}/repos/:owner/:repo/code-scanning/alerts?state=open&ref=<string>
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `state` | `string` | `Query` | `No` | Set to `closed` to list only closed code scanning alerts. |

| `ref` | `string` | `Query` | `No` | Returns a list of code scanning alerts for a specific brach reference. The `ref` must be formatted as `heads/<branch name>`. |



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
      "number": 42,
      "rule_id": "js/trivial-conditional",
      "rule_severity": "warning",
      "rule_description": "Useless conditional",
      "tool": "CodeQL",
      "created_at": "2020-05-06T12:00:00Z",
      "open": true,
      "closed_by": null,
      "closed_at": null,
      "url": "https://api.github.com/repos/Octo-org/octo-repo/code-scanning/alerts/25",
      "html_url": "https://github.com/Octo-org/octo-repo/security/code-scanning/25"
     },
     {
      "number": 43,
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
    ]
    ```


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

    Response if the ref doesn't match an existing ref

    ```json
    
    ```


