# {migration id}

API endpoints for {migration id}.

## Endpoints


### [archive](archive/index.md)

`` ``




### [Get an organization migration status](get-an-organization-migration-status.md)

`GET` `{{baseUrl}}/orgs/:org/migrations/:migration_id`

Fetches the status of a migration.

The `state` of a migration can be one of the following values:

...


### [Unlock an organization repository](unlock-an-organization-repository.md)

`DELETE` `{{baseUrl}}/orgs/:org/migrations/:migration_id/repos/:repo_name/lock`

Unlocks a repository that was locked for migration. You should unlock each migrated repository and [...


### [List repositories in an organization migration](list-repositories-in-an-organization-migration.md)

`GET` `{{baseUrl}}/orgs/:org/migrations/:migration_id/repositories?per_page=30&page=1`

List all the repositories for this organization migration....

