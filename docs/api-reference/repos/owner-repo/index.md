# {owner}/{repo}

API endpoints for {owner}/{repo}.

## Endpoints


### [actions](actions/index.md)

`` ``




### [assignees](assignees/index.md)

`` ``




### [automated-security-fixes](automated-security-fixes/index.md)

`` ``




### [branches](branches/index.md)

`` ``




### [check-runs](check-runs/index.md)

`` ``




### [check-suites](check-suites/index.md)

`` ``




### [code-scanning/alerts](code-scanning-alerts/index.md)

`` ``




### [collaborators](collaborators/index.md)

`` ``




### [comments](comments/index.md)

`` ``




### [commits](commits/index.md)

`` ``




### [community](community/index.md)

`` ``




### [contents/{path}](contents-path/index.md)

`` ``




### [deployments](deployments/index.md)

`` ``




### [forks](forks/index.md)

`` ``




### [git](git/index.md)

`` ``




### [hooks](hooks/index.md)

`` ``




### [import](import/index.md)

`` ``




### [interaction-limits](interaction-limits/index.md)

`` ``




### [invitations](invitations/index.md)

`` ``




### [issues](issues/index.md)

`` ``




### [keys](keys/index.md)

`` ``




### [labels](labels/index.md)

`` ``




### [milestones](milestones/index.md)

`` ``




### [notifications](notifications/index.md)

`` ``




### [pages](pages/index.md)

`` ``




### [projects](projects/index.md)

`` ``




### [pulls](pulls/index.md)

`` ``




### [releases](releases/index.md)

`` ``




### [stats](stats/index.md)

`` ``




### [subscription](subscription/index.md)

`` ``




### [topics](topics/index.md)

`` ``




### [traffic](traffic/index.md)

`` ``




### [vulnerability-alerts](vulnerability-alerts/index.md)

`` ``




### [Get a repository](get-a-repository.md)

`GET` `{{baseUrl}}/repos/:owner/:repo`

When you pass the `scarlet-witch-preview` media type, requests to get a repository will also return ...


### [Update a repository](update-a-repository.md)

`PATCH` `{{baseUrl}}/repos/:owner/:repo`

**Note**: To edit a repository's topics, use the [Replace all repository topics](https://developer.g...


### [Delete a repository](delete-a-repository.md)

`DELETE` `{{baseUrl}}/repos/:owner/:repo`

Deleting a repository requires admin access. If OAuth is used, the `delete_repo` scope is required.
...


### [Compare two commits](compare-two-commits.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/compare/{{base}}...{{head}}`

Both `:base` and `:head` must be branch names in `:repo`. To compare branches across other repositor...


### [List repository contributors](list-repository-contributors.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/contributors?anon=<string>&per_page=30&page=1`

Lists contributors to the specified repository and sorts them by the number of commits per contribut...


### [Create a repository dispatch event](create-a-repository-dispatch-event.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/dispatches`

You can use this endpoint to trigger a webhook event called `repository_dispatch` when you want acti...


### [List repository events](list-repository-events.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/events?per_page=30&page=1`

...


### [Get a repository installation for the authenticated app](get-a-repository-installation-for-the-authenticated-app.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/installation`

Enables an authenticated GitHub App to find the repository's installation information. The installat...


### [List repository languages](list-repository-languages.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/languages`

Lists languages for the specified repository. The value shown for each language is the number of byt...


### [Get the license for a repository](get-the-license-for-a-repository.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/license`

This method returns the contents of the repository's license file, if one is detected.

Similar to [...


### [Merge a branch](merge-a-branch.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/merges`

...


### [Get a repository README](get-a-repository-readme.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/readme?ref=<string>`

Gets the preferred README for a repository.

READMEs support [custom media types](https://developer....


### [List stargazers](list-stargazers.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/stargazers?per_page=30&page=1`

Lists the people that have starred the repository.

You can also find out _when_ stars were created ...


### [Create a commit status](create-a-commit-status.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/statuses/:sha`

Users with push access in a repository can create commit statuses for a given SHA.

Note: there is a...


### [List watchers](list-watchers.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/subscribers?per_page=30&page=1`

Lists the people watching the specified repository....


### [List repository tags](list-repository-tags.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/tags?per_page=30&page=1`

...


### [Download a repository archive (tar)](download-a-repository-archive-(tar).md)

`GET` `{{baseUrl}}/repos/:owner/:repo/tarball/:ref`

Gets a redirect URL to download a tar archive for a repository. If you omit `:ref`, the repository’s...


### [List repository teams](list-repository-teams.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/teams?per_page=30&page=1`

...


### [Transfer a repository](transfer-a-repository.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/transfer`

A transfer request will need to be accepted by the new owner when transferring a personal repository...


### [Download a repository archive (zip)](download-a-repository-archive-(zip).md)

`GET` `{{baseUrl}}/repos/:owner/:repo/zipball/:ref`

Gets a redirect URL to download a zip archive for a repository. If you omit `:ref`, the repository’s...

