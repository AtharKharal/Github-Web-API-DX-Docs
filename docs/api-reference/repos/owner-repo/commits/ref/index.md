# {ref}

API endpoints for {ref}.

## Endpoints


### [Get a commit](get-a-commit.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/commits/:ref`

Returns the contents of a single commit reference. You must have `read` access for the repository to...


### [List check runs for a Git reference](list-check-runs-for-a-git-reference.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/commits/:ref/check-runs?check_name=<string>&status=<string>&filter=latest&per_page=30&page=1`

**Note:** The Checks API only looks for pushes in the repository where the check suite or check run ...


### [List check suites for a Git reference](list-check-suites-for-a-git-reference.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/commits/:ref/check-suites?app_id=<integer>&check_name=<string>&per_page=30&page=1`

**Note:** The Checks API only looks for pushes in the repository where the check suite or check run ...


### [Get the combined status for a specific reference](get-the-combined-status-for-a-specific-reference.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/commits/:ref/status`

Users with pull access in a repository can access a combined view of commit statuses for a given ref...


### [List commit statuses for a reference](list-commit-statuses-for-a-reference.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/commits/:ref/statuses?per_page=30&page=1`

Users with pull access in a repository can view commit statuses for a given ref. The ref can be a SH...

