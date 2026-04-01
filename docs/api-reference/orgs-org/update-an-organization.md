# Update an organization

**Parameter Deprecation Notice:** GitHub will replace and discontinue `members_allowed_repository_creation_type` in favor of more granular permissions. The new input parameters are `members_can_create_public_repositories`, `members_can_create_private_repositories` for all organizations and `members_can_create_internal_repositories` for organizations associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+. For more information, see the [blog post](https://developer.github.com/changes/2019-12-03-internal-visibility-changes).

Enables an authenticated organization owner with the `admin:org` scope to update the organization's profile and member privileges.

```http
PATCH {{baseUrl}}/orgs/:org
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `org` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    {
        "billing_email": "<string>",
        "company": "<string>",
        "email": "<string>",
        "twitter_username": "<string>",
        "location": "<string>",
        "name": "<string>",
        "description": "<string>",
        "has_organization_projects": "<boolean>",
        "has_repository_projects": "<boolean>",
        "default_repository_permission": "read",
        "members_can_create_repositories": true,
        "members_can_create_internal_repositories": "<boolean>",
        "members_can_create_private_repositories": "<boolean>",
        "members_can_create_public_repositories": "<boolean>",
        "members_allowed_repository_creation_type": "<string>",
        "blog": "<string>"
    }
    ```


## Responses


=== "415 Unsupported Media Type"

    Preview Header Missing

    ```json
    {
     "message": "enim velit officia",
     "documentation_url": "et proident"
    }
    ```


=== "409 Conflict"

    Conflict

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "200 OK"

    response

    ```json
    {
     "login": "github",
     "id": 1,
     "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
     "url": "https://api.github.com/orgs/github",
     "repos_url": "https://api.github.com/orgs/github/repos",
     "events_url": "https://api.github.com/orgs/github/events",
     "hooks_url": "https://api.github.com/orgs/github/hooks",
     "issues_url": "https://api.github.com/orgs/github/issues",
     "members_url": "https://api.github.com/orgs/github/members{/member}",
     "public_members_url": "https://api.github.com/orgs/github/public_members{/member}",
     "avatar_url": "https://github.com/images/error/octocat_happy.gif",
     "description": "A great organization",
     "name": "github",
     "company": "GitHub",
     "blog": "https://github.com/blog",
     "location": "San Francisco",
     "email": "octocat@github.com",
     "twitter_username": "github",
     "is_verified": true,
     "has_organization_projects": true,
     "has_repository_projects": true,
     "public_repos": 2,
     "public_gists": 1,
     "followers": 20,
     "following": 0,
     "html_url": "https://github.com/octocat",
     "created_at": "2008-01-14T04:33:35Z",
     "type": "Organization",
     "total_private_repos": 100,
     "owned_private_repos": 100,
     "private_gists": 81,
     "disk_usage": 10000,
     "collaborators": 8,
     "billing_email": "mona@github.com",
     "plan": {
      "name": "Medium",
      "space": 400,
      "private_repos": 20
     },
     "default_repository_permission": "read",
     "members_can_create_repositories": true,
     "two_factor_requirement_enabled": true,
     "members_allowed_repository_creation_type": "all",
     "members_can_create_public_repositories": false,
     "members_can_create_private_repositories": false,
     "members_can_create_internal_repositories": false,
     "updated_at": "2014-03-03T18:58:10Z"
    }
    ```


=== "422 Unprocessable Entity (WebDAV) (RFC 4918)"

    Validation Failed

    ```json
    {
     "message": "culpa mollit",
     "documentation_url": "ipsum ut",
     "errors": [
      {
       "code": "consequat enim et velit",
       "resource": "anim ullamco",
       "field": "voluptate officia amet",
       "message": "exercitation sed dolore est",
       "index": 18359415,
       "value": "ullamco ut velit nulla eiusmod"
      },
      {
       "code": "occaecat eiusmod Duis",
       "resource": "esse ad Excepteur mollit",
       "field": "minim ipsum nisi exercitation non",
       "message": "proident reprehenderit",
       "index": -23326731,
       "value": "adipisicing cupidatat culpa in"
      }
     ]
    }
    ```


