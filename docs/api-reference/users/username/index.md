# {username}

API endpoints for {username}.

## Endpoints


### [events](events/index.md)

`` ``




### [following](following/index.md)

`` ``




### [received events](received-events/index.md)

`` ``




### [settings/billing](settings-billing/index.md)

`` ``




### [Get a user](get-a-user.md)

`GET` `{{baseUrl}}/users/:username`

Provides publicly available information about someone with a GitHub account.

GitHub Apps with the `...


### [List followers of a user](list-followers-of-a-user.md)

`GET` `{{baseUrl}}/users/:username/followers?per_page=30&page=1`

Lists the people following the specified user....


### [List gists for a user](list-gists-for-a-user.md)

`GET` `{{baseUrl}}/users/:username/gists?since=<string>&per_page=30&page=1`

Lists public gists for the specified user:...


### [List GPG keys for a user](list-gpg-keys-for-a-user.md)

`GET` `{{baseUrl}}/users/:username/gpg_keys?per_page=30&page=1`

Lists the GPG keys for a user. This information is accessible by anyone....


### [Get contextual information for a user](get-contextual-information-for-a-user.md)

`GET` `{{baseUrl}}/users/:username/hovercard?subject_type=<string>&subject_id=<string>`

Provides hovercard information when authenticated through basic auth or OAuth with the `repo` scope....


### [Get a user installation for the authenticated app](get-a-user-installation-for-the-authenticated-app.md)

`GET` `{{baseUrl}}/users/:username/installation`

Enables an authenticated GitHub App to find the user’s installation information.

You must use a [JW...


### [List public keys for a user](list-public-keys-for-a-user.md)

`GET` `{{baseUrl}}/users/:username/keys?per_page=30&page=1`

Lists the _verified_ public SSH keys for a user. This is accessible by anyone....


### [List organizations for a user](list-organizations-for-a-user.md)

`GET` `{{baseUrl}}/users/:username/orgs?per_page=30&page=1`

List [public organization memberships](https://help.github.com/articles/publicizing-or-concealing-or...


### [List user projects](list-user-projects.md)

`GET` `{{baseUrl}}/users/:username/projects?state=open&per_page=30&page=1`

...


### [List repositories for a user](list-repositories-for-a-user.md)

`GET` `{{baseUrl}}/users/:username/repos?type=owner&sort=full_name&direction=<string>&per_page=30&page=1`

Lists public repositories for the specified user....


### [List repositories starred by a user](list-repositories-starred-by-a-user.md)

`GET` `{{baseUrl}}/users/:username/starred?sort=created&direction=desc&per_page=30&page=1`

Lists repositories a user has starred.

You can also find out _when_ stars were created by passing t...


### [List repositories watched by a user](list-repositories-watched-by-a-user.md)

`GET` `{{baseUrl}}/users/:username/subscriptions?per_page=30&page=1`

Lists repositories a user is watching....

