# {migration id}

API endpoints for {migration id}.

## Endpoints


### [archive](archive/index.md)

`` ``




### [Get a user migration status](get-a-user-migration-status.md)

`GET` `{{baseUrl}}/user/migrations/:migration_id?exclude=<string>&exclude=<string>`

Fetches a single user migration. The response includes the `state` of the migration, which can be on...


### [Unlock a user repository](unlock-a-user-repository.md)

`DELETE` `{{baseUrl}}/user/migrations/:migration_id/repos/:repo_name/lock`

Unlocks a repository. You can lock repositories when you [start a user migration](https://developer....


### [List repositories for a user migration](list-repositories-for-a-user-migration.md)

`GET` `{{baseUrl}}/user/migrations/:migration_id/repositories?per_page=30&page=1`

Lists all the repositories for this user migration....

