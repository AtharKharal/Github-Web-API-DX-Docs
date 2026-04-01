# {issue number}

API endpoints for {issue number}.

## Endpoints


### [assignees](assignees/index.md)

`` ``




### [comments](comments/index.md)

`` ``




### [labels](labels/index.md)

`` ``




### [lock](lock/index.md)

`` ``




### [reactions](reactions/index.md)

`` ``




### [Get an issue](get-an-issue.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/issues/:issue_number`

The API returns a [`301 Moved Permanently` status](https://developer.github.com/v3/#http-redirects) ...


### [Update an issue](update-an-issue.md)

`PATCH` `{{baseUrl}}/repos/:owner/:repo/issues/:issue_number`

Issue owners and users with push access can edit an issue....


### [List issue events](list-issue-events.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/issues/:issue_number/events?per_page=30&page=1`

...


### [List timeline events for an issue](list-timeline-events-for-an-issue.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/issues/:issue_number/timeline?per_page=30&page=1`

...

