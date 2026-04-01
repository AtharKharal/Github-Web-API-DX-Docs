# {username}

API endpoints for {username}.

## Endpoints


### [Check if a user is a repository collaborator](check-if-a-user-is-a-repository-collaborator.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/collaborators/:username`

For organization-owned repositories, the list of collaborators includes outside collaborators, organ...


### [Add a repository collaborator](add-a-repository-collaborator.md)

`PUT` `{{baseUrl}}/repos/:owner/:repo/collaborators/:username`

This endpoint triggers [notifications](https://help.github.com/articles/about-notifications/). Creat...


### [Remove a repository collaborator](remove-a-repository-collaborator.md)

`DELETE` `{{baseUrl}}/repos/:owner/:repo/collaborators/:username`

...


### [Get repository permissions for a user](get-repository-permissions-for-a-user.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/collaborators/:username/permission`

Checks the repository permission of a collaborator. The possible repository permissions are `admin`,...

