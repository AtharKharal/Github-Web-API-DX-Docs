# {check suite id}

API endpoints for {check suite id}.

## Endpoints


### [Get a check suite](get-a-check-suite.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/check-suites/:check_suite_id`

**Note:** The Checks API only looks for pushes in the repository where the check suite or check run ...


### [List check runs in a check suite](list-check-runs-in-a-check-suite.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/check-suites/:check_suite_id/check-runs?check_name=<string>&status=<string>&filter=latest&per_page=30&page=1`

**Note:** The Checks API only looks for pushes in the repository where the check suite or check run ...


### [Rerequest a check suite](rerequest-a-check-suite.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/check-suites/:check_suite_id/rerequest`

Triggers GitHub to rerequest an existing check suite, without pushing new code to a repository. This...

