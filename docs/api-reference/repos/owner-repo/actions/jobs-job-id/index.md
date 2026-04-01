# jobs/{job id}

API endpoints for jobs/{job id}.

## Endpoints


### [Get a job for a workflow run](get-a-job-for-a-workflow-run.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/actions/jobs/:job_id`

Gets a specific job in a workflow run. Anyone with read access to the repository can use this endpoi...


### [Download job logs for a workflow run](download-job-logs-for-a-workflow-run.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/actions/jobs/:job_id/logs`

Gets a redirect URL to download a plain text file of logs for a workflow job. This link expires afte...

