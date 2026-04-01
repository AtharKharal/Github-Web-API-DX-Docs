# {artifact id}

API endpoints for {artifact id}.

## Endpoints


### [Get an artifact](get-an-artifact.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/actions/artifacts/:artifact_id`

Gets a specific artifact for a workflow run. Anyone with read access to the repository can use this ...


### [Delete an artifact](delete-an-artifact.md)

`DELETE` `{{baseUrl}}/repos/:owner/:repo/actions/artifacts/:artifact_id`

Deletes an artifact for a workflow run. You must authenticate using an access token with the `repo` ...


### [Download an artifact](download-an-artifact.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/actions/artifacts/:artifact_id/:archive_format`

Gets a redirect URL to download an archive for a repository. This URL expires after 1 minute. Look f...

