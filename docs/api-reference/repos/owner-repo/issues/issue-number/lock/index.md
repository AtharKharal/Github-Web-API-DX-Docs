# lock

API endpoints for lock.

## Endpoints


### [Lock an issue](lock-an-issue.md)

`PUT` `{{baseUrl}}/repos/:owner/:repo/issues/:issue_number/lock`

Users with push access can lock an issue or pull request's conversation.

Note that, if you choose n...


### [Unlock an issue](unlock-an-issue.md)

`DELETE` `{{baseUrl}}/repos/:owner/:repo/issues/:issue_number/lock`

Users with push access can unlock an issue's conversation....

