# labels

API endpoints for labels.

## Endpoints


### [List labels for an issue](list-labels-for-an-issue.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/issues/:issue_number/labels?per_page=30&page=1`

...


### [Add labels to an issue](add-labels-to-an-issue.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/issues/:issue_number/labels`

...


### [Set labels for an issue](set-labels-for-an-issue.md)

`PUT` `{{baseUrl}}/repos/:owner/:repo/issues/:issue_number/labels`

Removes any previous labels and sets the new labels for an issue....


### [Remove all labels from an issue](remove-all-labels-from-an-issue.md)

`DELETE` `{{baseUrl}}/repos/:owner/:repo/issues/:issue_number/labels`

...


### [Remove a label from an issue](remove-a-label-from-an-issue.md)

`DELETE` `{{baseUrl}}/repos/:owner/:repo/issues/:issue_number/labels/:name`

Removes the specified label from the issue, and returns the remaining labels on the issue. This endp...

