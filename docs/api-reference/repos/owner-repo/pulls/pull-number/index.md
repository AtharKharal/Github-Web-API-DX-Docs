# {pull number}

API endpoints for {pull number}.

## Endpoints


### [comments](comments/index.md)

`` ``




### [merge](merge/index.md)

`` ``




### [requested reviewers](requested-reviewers/index.md)

`` ``




### [reviews](reviews/index.md)

`` ``




### [Get a pull request](get-a-pull-request.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/pulls/:pull_number`

Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organi...


### [Update a pull request](update-a-pull-request.md)

`PATCH` `{{baseUrl}}/repos/:owner/:repo/pulls/:pull_number`

Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organi...


### [List commits on a pull request](list-commits-on-a-pull-request.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/pulls/:pull_number/commits?per_page=30&page=1`

Lists a maximum of 250 commits for a pull request. To receive a complete commit list for pull reques...


### [List pull requests files](list-pull-requests-files.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/pulls/:pull_number/files?per_page=30&page=1`

**Note:** Responses include a maximum of 3000 files. The paginated response returns 30 files per pag...


### [Update a pull request branch](update-a-pull-request-branch.md)

`PUT` `{{baseUrl}}/repos/:owner/:repo/pulls/:pull_number/update-branch`

Updates the pull request branch with the latest upstream changes by merging HEAD from the base branc...

