# {commit sha}

API endpoints for {commit sha}.

## Endpoints


### [comments](comments/index.md)

`` ``




### [List branches for HEAD commit](list-branches-for-head-commit.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/commits/:commit_sha/branches-where-head`

Protected branches are available in public repositories with GitHub Free and GitHub Free for organiz...


### [List pull requests associated with a commit](list-pull-requests-associated-with-a-commit.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/commits/:commit_sha/pulls?per_page=30&page=1`

Lists all pull requests containing the provided commit SHA, which can be from any point in the commi...

