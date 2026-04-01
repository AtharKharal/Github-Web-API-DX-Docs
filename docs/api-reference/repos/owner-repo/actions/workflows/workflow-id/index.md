# {workflow id}

API endpoints for {workflow id}.

## Endpoints


### [Get a workflow](get-a-workflow.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/actions/workflows/:workflow_id`

Gets a specific workflow. You can also replace `:workflow_id` with `:workflow_file_name`. For exampl...


### [Create a workflow dispatch event](create-a-workflow-dispatch-event.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/actions/workflows/:workflow_id/dispatches`

You can use this endpoint to manually trigger a GitHub Actions workflow run. You can also replace `{...


### [List workflow runs](list-workflow-runs.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/actions/workflows/:workflow_id/runs?actor=<string>&branch=<string>&event=<string>&status=<string>&per_page=30&page=1`

List all workflow runs for a workflow. You can also replace `:workflow_id` with `:workflow_file_name...


### [Get workflow usage](get-workflow-usage.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/actions/workflows/:workflow_id/timing`

**Warning:** This GitHub Actions usage endpoint is currently in public beta and subject to change. F...

