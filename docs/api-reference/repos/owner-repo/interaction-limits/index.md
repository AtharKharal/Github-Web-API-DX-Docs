# interaction-limits

API endpoints for interaction-limits.

## Endpoints


### [Get interaction restrictions for a repository](get-interaction-restrictions-for-a-repository.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/interaction-limits`

Shows which group of GitHub users can interact with this repository and when the restriction expires...


### [Set interaction restrictions for a repository](set-interaction-restrictions-for-a-repository.md)

`PUT` `{{baseUrl}}/repos/:owner/:repo/interaction-limits`

Temporarily restricts interactions to certain GitHub users within the given repository. You must hav...


### [Remove interaction restrictions for a repository](remove-interaction-restrictions-for-a-repository.md)

`DELETE` `{{baseUrl}}/repos/:owner/:repo/interaction-limits`

Removes all interaction restrictions from the given repository. You must have owner or admin access ...

