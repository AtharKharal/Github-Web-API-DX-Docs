# logs

API endpoints for logs.

## Endpoints


### [Download workflow run logs](download-workflow-run-logs.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/actions/runs/:run_id/logs`

Gets a redirect URL to download an archive of log files for a workflow run. This link expires after ...


### [Delete workflow run logs](delete-workflow-run-logs.md)

`DELETE` `{{baseUrl}}/repos/:owner/:repo/actions/runs/:run_id/logs`

Deletes all logs for a workflow run. You must authenticate using an access token with the `repo` sco...

