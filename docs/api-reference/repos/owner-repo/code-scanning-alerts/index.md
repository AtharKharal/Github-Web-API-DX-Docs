# code-scanning/alerts

API endpoints for code-scanning/alerts.

## Endpoints


### [List code scanning alerts for a repository](list-code-scanning-alerts-for-a-repository.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/code-scanning/alerts?state=open&ref=<string>`

Lists all open code scanning alerts for the default branch (usually `master`) and protected branches...


### [Get a code scanning alert](get-a-code-scanning-alert.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/code-scanning/alerts/:alert_id`

Gets a single code scanning alert. You must use an access token with the `security_events` scope to ...

