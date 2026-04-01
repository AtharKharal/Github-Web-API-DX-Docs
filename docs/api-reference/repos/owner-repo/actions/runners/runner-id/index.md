# {runner id}

API endpoints for {runner id}.

## Endpoints


### [Get a self-hosted runner for a repository](get-a-self-hosted-runner-for-a-repository.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/actions/runners/:runner_id`

Gets a specific self-hosted runner. You must authenticate using an access token with the `repo` scop...


### [Delete a self-hosted runner from a repository](delete-a-self-hosted-runner-from-a-repository.md)

`DELETE` `{{baseUrl}}/repos/:owner/:repo/actions/runners/:runner_id`

Forces the removal of a self-hosted runner from a repository. You can use this endpoint to completel...

