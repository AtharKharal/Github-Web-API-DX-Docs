# {run id}

API endpoints for {run id}.

## Endpoints


### [logs](logs/index.md)

`` ``




### [Get a workflow run](get-a-workflow-run.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/actions/runs/:run_id`

Gets a specific workflow run. Anyone with read access to the repository can use this endpoint. If th...


### [Delete a workflow run](delete-a-workflow-run.md)

`DELETE` `{{baseUrl}}/repos/:owner/:repo/actions/runs/:run_id`

Delete a specific workflow run. Anyone with write access to the repository can use this endpoint. If...


### [List workflow run artifacts](list-workflow-run-artifacts.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/actions/runs/:run_id/artifacts?per_page=30&page=1`

Lists artifacts for a workflow run. Anyone with read access to the repository can use this endpoint....


### [Cancel a workflow run](cancel-a-workflow-run.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/actions/runs/:run_id/cancel`

Cancels a workflow run using its `id`. You must authenticate using an access token with the `repo` s...


### [List jobs for a workflow run](list-jobs-for-a-workflow-run.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/actions/runs/:run_id/jobs?filter=latest&per_page=30&page=1`

Lists jobs for a workflow run. Anyone with read access to the repository can use this endpoint. If t...


### [Re-run a workflow](re-run-a-workflow.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/actions/runs/:run_id/rerun`

Re-runs your workflow run using its `id`. You must authenticate using an access token with the `repo...


### [Get workflow run usage](get-workflow-run-usage.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/actions/runs/:run_id/timing`

**Warning:** This GitHub Actions usage endpoint is currently in public beta and subject to change. F...

