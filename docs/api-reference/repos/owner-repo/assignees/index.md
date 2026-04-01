# assignees

API endpoints for assignees.

## Endpoints


### [List assignees](list-assignees.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/assignees?per_page=30&page=1`

Lists the [available assignees](https://help.github.com/articles/assigning-issues-and-pull-requests-...


### [Check if a user can be assigned](check-if-a-user-can-be-assigned.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/assignees/:assignee`

Checks if a user has permission to be assigned to an issue in this repository.

If the `assignee` ca...

