# Update branch protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Protecting a branch requires admin or owner permissions to the repository.

**Note**: Passing new arrays of `users` and `teams` replaces their previous values.

**Note**: The list of users, apps, and teams in total is limited to 100 items.

```http
PUT {{baseUrl}}/repos/:owner/:repo/branches/:branch/protection
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `branch` | `string` | `Path` | `Yes` | (Required) branch+ parameter |



## Request Body

=== "JSON"

    ```json
    {
        "required_status_checks": {
            "strict": "<boolean>",
            "contexts": [
                "<string>",
                "<string>"
            ]
        },
        "enforce_admins": "<boolean>",
        "required_pull_request_reviews": {
            "dismissal_restrictions": {
                "users": [
                    "<string>",
                    "<string>"
                ],
                "teams": [
                    "<string>",
                    "<string>"
                ]
            },
            "dismiss_stale_reviews": "<boolean>",
            "require_code_owner_reviews": "<boolean>",
            "required_approving_review_count": "<integer>"
        },
        "restrictions": {
            "users": [
                "<string>",
                "<string>"
            ],
            "teams": [
                "<string>",
                "<string>"
            ],
            "apps": [
                "<string>",
                "<string>"
            ]
        },
        "required_linear_history": "<boolean>",
        "allow_force_pushes": "<boolean>",
        "allow_deletions": "<boolean>"
    }
    ```


## Responses


=== "403 Forbidden"

    Forbidden

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "415 Unsupported Media Type"

    Preview Header Missing

    ```json
    {
     "message": "enim velit officia",
     "documentation_url": "et proident"
    }
    ```


=== "200 OK"

    response

    ```json
    {
     "url": "deserunt consectetur do",
     "required_status_checks": {
      "url": "https://api.github.com/repos/octocat/Hello-World/branches/master/protection/required_status_checks",
      "contexts_url": "https://api.github.com/repos/octocat/Hello-World/branches/master/protection/required_status_checks/contexts",
      "strict": true,
      "contexts": [
       "continuous-integration/travis-ci"
      ]
     },
     "required_pull_request_reviews": {
      "url": "anim labore",
      "dismiss_stale_reviews": false,
      "require_code_owner_reviews": false,
      "required_approving_review_count": -56907738,
      "dismissal_restrictions": {
       "url": "adipisicing Ut",
       "users_url": "Ut id consectetur ipsum",
       "teams_url": "cupidatat et voluptate ut incididunt",
       "users": [
        {
         "avatar_url": "https://github.com/images/error/octocat_happy.gif",
         "events_url": "https://api.github.com/users/octocat/events{/privacy}",
         "followers_url": "https://api.github.com/users/octocat/followers",
         "following_url": "https://api.github.com/users/octocat/following{/other_user}",
         "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
         "gravatar_id": "",
         "html_url": "https://github.com/octocat",
         "id": 1,
         "node_id": "MDQ6VXNlcjE=",
         "login": "octocat",
         "organizations_url": "https://api.github.com/users/octocat/orgs",
         "received_events_url": "https://api.github.com/users/octocat/received_events",
         "repos_url": "https://api.github.com/users/octocat/repos",
         "site_admin": true,
         "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
         "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
         "type": "User",
         "url": "https://api.github.com/users/octocat",
         "starred_at": "\"2020-07-09T00:17:55Z\""
        },
        {
         "avatar_url": "https://github.com/images/error/octocat_happy.gif",
         "events_url": "https://api.github.com/users/octocat/events{/privacy}",
         "followers_url": "https://api.github.com/users/octocat/followers",
         "following_url": "https://api.github.com/users/octocat/following{/other_user}",
         "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
         "gravatar_id": "",
         "html_url": "https://github.com/octocat",
         "id": 1,
         "node_id": "MDQ6VXNlcjE=",
         "login": "octocat",
         "organizations_url": "https://api.github.com/users/octocat/orgs",
         "received_events_url": "https://api.github.com/users/octocat/received_events",
         "repos_url": "https://api.github.com/users/octocat/repos",
         "site_admin": true,
         "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
         "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
         "type": "User",
         "url": "https://api.github.com/users/octocat",
         "starred_at": "\"2020-07-09T00:17:55Z\""
        }
       ],
       "teams": [
        {
         "id": -98654282,
         "node_id": "dolor Ut officia ad",
         "url": "qui ex mollit sit enim",
         "members_url": "minim consectetur",
         "name": "consequat",
         "description": "adipisicing tempor fugiat proident",
         "permission": "voluptate ex ut",
         "html_url": "https://github.com/orgs/rails/teams/core",
         "repositories_url": "ex Excepteur officia ut",
         "slug": "reprehenderit adipis",
         "privacy": "aliquip ea",
         "parent": {
          "id": 1,
          "node_id": "MDQ6VGVhbTE=",
          "url": "https://api.github.com/organizations/1/team/1",
          "members_url": "https://api.github.com/organizations/1/team/1/members{/member}",
          "name": "Justice League",
          "description": "A great team.",
          "permission": "admin",
          "html_url": "https://github.com/orgs/rails/teams/core",
          "repositories_url": "https://api.github.com/organizations/1/team/1/repos",
          "slug": "justice-league",
          "privacy": "closed",
          "ldap_dn": "uid=example,ou=users,dc=github,dc=com"
         }
        },
        {
         "id": 33624176,
         "node_id": "sunt",
         "url": "aute aliquip labore cillum",
         "members_url": "id Ut enim",
         "name": "ipsum proident consequat",
         "description": "in esse commodo",
         "permission": "officia elit",
         "html_url": "https://github.com/orgs/rails/teams/core",
         "repositories_url": "aliquip esse commodo tempor",
         "slug": "elit qui nisi ut",
         "privacy": "eu ess",
         "parent": {
          "id": 1,
          "node_id": "MDQ6VGVhbTE=",
          "url": "https://api.github.com/organizations/1/team/1",
          "members_url": "https://api.github.com/organizations/1/team/1/members{/member}",
          "name": "Justice League",
          "description": "A great team.",
          "permission": "admin",
          "html_url": "https://github.com/orgs/rails/teams/core",
          "repositories_url": "https://api.github.com/organizations/1/team/1/repos",
          "slug": "justice-league",
          "privacy": "closed",
          "ldap_dn": "uid=example,ou=users,dc=github,dc=com"
         }
        }
       ]
      }
     },
     "required_signatures": {
      "url": "https://api.github.com/repos/octocat/Hello-World/branches/master/protection/required_signatures",
      "enabled": true
     },
     "enforce_admins": {
      "url": "ut quis tempor",
      "enabled": true
     },
     "required_linear_history": {
      "enabled": false
     },
     "allow_force_pushes": {
      "enabled": true
     },
     "allow_deletions": {
      "enabled": false
     },
     "restrictions": {
      "url": "in occaecat",
      "users_url": "dolor nisi ex quis exercitation",
      "teams_url": "elit dolore in ex",
      "apps_url": "et quis sint cu",
      "users": [
       {
        "login": "laboris deserunt tempo",
        "id": -93347071,
        "node_id": "aliquip irure",
        "avatar_url": "aliqua dolore dese",
        "gravatar_id": "labore cupidatat ipsum",
        "url": "est tempor quis",
        "html_url": "pariatur velit",
        "followers_url": "elit sit",
        "following_url": "consectetur nisi ad sed",
        "gists_url": "sed Lorem eu fugiat",
        "starred_url": "occaecat pariatur",
        "subscriptions_url": "velit qui dolore",
        "organizations_url": "elit dolore tempor eu quis",
        "repos_url": "velit mollit l",
        "events_url": "id ex commodo sint",
        "received_events_url": "in",
        "type": "nisi dolor et",
        "site_admin": false
       },
       {
        "login": "reprehenderit ad in labore Duis",
        "id": -19448178,
        "node_id": "id dolor est",
        "avatar_url": "culpa Duis",
        "gravatar_id": "mollit nostrud",
        "url": "enim veniam reprehenderit",
        "html_url": "in magna exercitation",
        "followers_url": "cillum velit officia aute",
        "following_url": "fugiat commodo et d",
        "gists_url": "consequat pariatur",
        "starred_url": "laboris reprehenderit esse",
        "subscriptions_url": "tempor occaecat amet",
        "organizations_url": "ipsum consequat",
        "repos_url": "ullamco eu",
        "events_url": "dolor",
        "received_events_url": "enim",
        "type": "qui est",
        "site_admin": true
       }
      ],
      "teams": [
       {
        "id": 71159569,
        "node_id": "ea",
        "url": "eiusmod aute",
        "html_url": "aute",
        "name": "anim voluptate ut",
        "slug": "in mollit",
        "description": "officia",
        "privacy": "deserunt eiusmod irure officia",
        "permission": "sed",
        "members_url": "tempor aute ",
        "repositories_url": "qui deseru",
        "parent": "ea ipsum sit"
       },
       {
        "id": -72381659,
        "node_id": "dolore officia irure minim",
        "url": "ipsum sed",
        "html_url": "ut",
        "name": "nulla dolor ad elit",
        "slug": "laboris ipsum adipisicing reprehenderit cillum",
        "description": "eiusmod",
        "privacy": "in consectetur ut",
        "permission": "ad labore pariatur",
        "members_url": "id Ut cupidatat",
        "repositories_url": "culpa ad adipisicing reprehenderit",
        "parent": "tempor n"
       }
      ],
      "apps": [
       {
        "id": -9035988,
        "slug": "laboris esse in",
        "node_id": "ipsum qui p",
        "owner": {
         "login": "deserunt sint reprehenderit incididunt",
         "id": 31501709,
         "node_id": "tempor aliquip ",
         "url": "dolore pariatur occaecat sunt",
         "repos_url": "dolor in nostrud",
         "events_url": "magna sed sint",
         "hooks_url": "veniam adipisicing fugiat",
         "issues_url": "cillum minim",
         "members_url": "occaecat",
         "public_members_url": "consequat ani",
         "avatar_url": "in proident",
         "description": "ullamco laboris do velit elit",
         "gravatar_id": "\"\"",
         "html_url": "\"https://github.com/testorg-ea8ec76d71c3af4b\"",
         "followers_url": "\"https://api.github.com/users/testorg-ea8ec76d71c3af4b/followers\"",
         "following_url": "\"https://api.github.com/users/testorg-ea8ec76d71c3af4b/following{/other_user}\"",
         "gists_url": "\"https://api.github.com/users/testorg-ea8ec76d71c3af4b/gists{/gist_id}\"",
         "starred_url": "\"https://api.github.com/users/testorg-ea8ec76d71c3af4b/starred{/owner}{/repo}\"",
         "subscriptions_url": "\"https://api.github.com/users/testorg-ea8ec76d71c3af4b/subscriptions\"",
         "organizations_url": "\"https://api.github.com/users/testorg-ea8ec76d71c3af4b/orgs\"",
         "received_events_url": "\"https://api.github.com/users/testorg-ea8ec76d71c3af4b/received_events\"",
         "type": "\"Organization\""
        },
        "name": "culpa cillum",
        "description": "dolore proident ut",
        "external_url": "laborum deserunt",
        "html_url": "anim magna eiusmod i",
        "created_at": "labore quis minim dolore",
        "updated_at": "labore cillum Lorem",
        "permissions": {
         "metadata": "veniam anim aliquip consequat",
         "contents": "non velit",
         "issues": "non eiusmod elit",
         "single_file": "esse sint Excepteur cupidatat ut"
        },
        "events": [
         "minim consequat",
         "dolor esse ipsum pariatur cupidatat"
        ]
       },
       {
        "id": 69184777,
        "slug": "quis officia Excepteur",
        "node_id": "ea",
        "owner": {
         "login": "deserunt veniam",
         "id": -5725275,
         "node_id": "eiusmod dolore",
         "url": "deserunt adipisicing dolore",
         "repos_url": "reprehenderit dolore",
         "events_url": "ut magna in minim",
         "hooks_url": "ipsum",
         "issues_url": "in minim nostrud",
         "members_url": "irure elit non",
         "public_members_url": "consectetur aute",
         "avatar_url": "nulla",
         "description": "reprehenderit Excepteur sit",
         "gravatar_id": "\"\"",
         "html_url": "\"https://github.com/testorg-ea8ec76d71c3af4b\"",
         "followers_url": "\"https://api.github.com/users/testorg-ea8ec76d71c3af4b/followers\"",
         "following_url": "\"https://api.github.com/users/testorg-ea8ec76d71c3af4b/following{/other_user}\"",
         "gists_url": "\"https://api.github.com/users/testorg-ea8ec76d71c3af4b/gists{/gist_id}\"",
         "starred_url": "\"https://api.github.com/users/testorg-ea8ec76d71c3af4b/starred{/owner}{/repo}\"",
         "subscriptions_url": "\"https://api.github.com/users/testorg-ea8ec76d71c3af4b/subscriptions\"",
         "organizations_url": "\"https://api.github.com/users/testorg-ea8ec76d71c3af4b/orgs\"",
         "received_events_url": "\"https://api.github.com/users/testorg-ea8ec76d71c3af4b/received_events\"",
         "type": "\"Organization\""
        },
        "name": "sit Ut",
        "description": "mollit proident",
        "external_url": "non proi",
        "html_url": "in sunt",
        "created_at": "in quis exercitation veniam reprehenderit",
        "updated_at": "nostrud sint voluptate",
        "permissions": {
         "metadata": "laboris nisi Excepteur labore",
         "contents": "sit deserunt",
         "issues": "nostrud officia cillum est dolore",
         "single_file": "ut"
        },
        "events": [
         "ex et",
         "in officia esse"
        ]
       }
      ]
     }
    }
    ```


=== "422 Unprocessable Entity (WebDAV) (RFC 4918)"

    Validation Failed

    ```json
    {
     "message": "in labore deserunt nostrud amet",
     "documentation_url": "Duis",
     "errors": [
      "nisi dolore Ut",
      "est culpa ullamco voluptate"
     ]
    }
    ```


=== "404 Not Found"

    Resource Not Found

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


