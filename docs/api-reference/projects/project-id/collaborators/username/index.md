# {username}

API endpoints for {username}.

## Endpoints


### [Add project collaborator](add-project-collaborator.md)

`PUT` `{{baseUrl}}/projects/:project_id/collaborators/:username`

Adds a collaborator to an organization project and sets their permission level. You must be an organ...


### [Remove user as a collaborator](remove-user-as-a-collaborator.md)

`DELETE` `{{baseUrl}}/projects/:project_id/collaborators/:username`

Removes a collaborator from an organization project. You must be an organization owner or a project ...


### [Get project permission for a user](get-project-permission-for-a-user.md)

`GET` `{{baseUrl}}/projects/:project_id/collaborators/:username/permission`

Returns the collaborator's permission level for an organization project. Possible values for the `pe...

