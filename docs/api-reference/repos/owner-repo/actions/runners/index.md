# runners

API endpoints for runners.

## Endpoints


### [{runner id}](runner-id/index.md)

`` ``




### [List self-hosted runners for a repository](list-self-hosted-runners-for-a-repository.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/actions/runners?per_page=30&page=1`

Lists all self-hosted runners for a repository. You must authenticate using an access token with the...


### [List runner applications for a repository](list-runner-applications-for-a-repository.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/actions/runners/downloads`

Lists binaries for the runner application that you can download and run. You must authenticate using...


### [Create a registration token for a repository](create-a-registration-token-for-a-repository.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/actions/runners/registration-token`

Returns a token that you can pass to the `config` script. The token expires after one hour. You must...


### [Create a remove token for a repository](create-a-remove-token-for-a-repository.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/actions/runners/remove-token`

Returns a token that you can pass to remove a self-hosted runner from a repository. The token expire...

