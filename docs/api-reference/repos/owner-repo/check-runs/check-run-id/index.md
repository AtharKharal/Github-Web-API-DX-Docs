# {check run id}

API endpoints for {check run id}.

## Endpoints


### [Get a check run](get-a-check-run.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/check-runs/:check_run_id`

**Note:** The Checks API only looks for pushes in the repository where the check suite or check run ...


### [Update a check run](update-a-check-run.md)

`PATCH` `{{baseUrl}}/repos/:owner/:repo/check-runs/:check_run_id`

**Note:** The Checks API only looks for pushes in the repository where the check suite or check run ...


### [List check run annotations](list-check-run-annotations.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/check-runs/:check_run_id/annotations?per_page=30&page=1`

Lists annotations for a check run using the annotation `id`. GitHub Apps must have the `checks:read`...

