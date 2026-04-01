# archive

API endpoints for archive.

## Endpoints


### [Download a user migration archive](download-a-user-migration-archive.md)

`GET` `{{baseUrl}}/user/migrations/:migration_id/archive`

Fetches the URL to download the migration archive as a `tar.gz` file. Depending on the resources you...


### [Delete a user migration archive](delete-a-user-migration-archive.md)

`DELETE` `{{baseUrl}}/user/migrations/:migration_id/archive`

Deletes a previous migration archive. Downloadable migration archives are automatically deleted afte...

