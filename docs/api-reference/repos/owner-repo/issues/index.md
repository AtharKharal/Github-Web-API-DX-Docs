# issues

API endpoints for issues.

## Endpoints


### [comments](comments/index.md)

`` ``




### [events](events/index.md)

`` ``




### [{issue number}](issue-number/index.md)

`` ``




### [List repository issues](list-repository-issues.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/issues?milestone=<string>&state=open&assignee=<string>&creator=<string>&mentioned=<string>&labels=<string>&sort=created&direction=desc&since=<string>&per_page=30&page=1`

List issues in a repository.

**Note**: GitHub's REST API v3 considers every pull request an issue, ...


### [Create an issue](create-an-issue.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/issues`

Any user with pull access to a repository can create an issue. If [issues are disabled in the reposi...

