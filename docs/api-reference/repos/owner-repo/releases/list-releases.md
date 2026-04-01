# List releases

This returns a list of releases, which does not include regular Git tags that have not been associated with a release. To get a list of Git tags, use the [Repository Tags API](https://developer.github.com/v3/repos/#list-repository-tags).

Information about published releases are available to everyone. Only users with push access will receive listings for draft releases.

```http
GET {{baseUrl}}/repos/:owner/:repo/releases?per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `per_page` | `string` | `Query` | `No` | Results per page (max 100) |

| `page` | `string` | `Query` | `No` | Page number of the results to fetch. |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "200 OK"

    response

    ```json
    [
     {
      "url": "https://api.github.com/repos/octocat/Hello-World/releases/1",
      "html_url": "https://github.com/octocat/Hello-World/releases/v1.0.0",
      "assets_url": "https://api.github.com/repos/octocat/Hello-World/releases/1/assets",
      "upload_url": "https://uploads.github.com/repos/octocat/Hello-World/releases/1/assets{?name,label}",
      "tarball_url": "https://api.github.com/repos/octocat/Hello-World/tarball/v1.0.0",
      "zipball_url": "https://api.github.com/repos/octocat/Hello-World/zipball/v1.0.0",
      "id": 1,
      "node_id": "MDc6UmVsZWFzZTE=",
      "tag_name": "v1.0.0",
      "target_commitish": "master",
      "name": "v1.0.0",
      "body": "Description of the release",
      "draft": false,
      "prerelease": false,
      "created_at": "2013-02-27T19:35:32Z",
      "published_at": "2013-02-27T19:35:32Z",
      "author": {
       "login": "octocat",
       "id": 1,
       "node_id": "MDQ6VXNlcjE=",
       "avatar_url": "https://github.com/images/error/octocat_happy.gif",
       "gravatar_id": "",
       "url": "https://api.github.com/users/octocat",
       "html_url": "https://github.com/octocat",
       "followers_url": "https://api.github.com/users/octocat/followers",
       "following_url": "https://api.github.com/users/octocat/following{/other_user}",
       "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
       "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
       "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
       "organizations_url": "https://api.github.com/users/octocat/orgs",
       "repos_url": "https://api.github.com/users/octocat/repos",
       "events_url": "https://api.github.com/users/octocat/events{/privacy}",
       "received_events_url": "https://api.github.com/users/octocat/received_events",
       "type": "User",
       "site_admin": false
      },
      "assets": [
       {
        "url": "https://api.github.com/repos/octocat/Hello-World/releases/assets/1",
        "browser_download_url": "https://github.com/octocat/Hello-World/releases/download/v1.0.0/example.zip",
        "id": 1,
        "node_id": "MDEyOlJlbGVhc2VBc3NldDE=",
        "name": "example.zip",
        "label": "short description",
        "state": "uploaded",
        "content_type": "application/zip",
        "size": 1024,
        "download_count": 42,
        "created_at": "2013-02-27T19:35:32Z",
        "updated_at": "2013-02-27T19:35:32Z",
        "uploader": {
         "login": "octocat",
         "id": 1,
         "node_id": "MDQ6VXNlcjE=",
         "avatar_url": "https://github.com/images/error/octocat_happy.gif",
         "gravatar_id": "",
         "url": "https://api.github.com/users/octocat",
         "html_url": "https://github.com/octocat",
         "followers_url": "https://api.github.com/users/octocat/followers",
         "following_url": "https://api.github.com/users/octocat/following{/other_user}",
         "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
         "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
         "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
         "organizations_url": "https://api.github.com/users/octocat/orgs",
         "repos_url": "https://api.github.com/users/octocat/repos",
         "events_url": "https://api.github.com/users/octocat/events{/privacy}",
         "received_events_url": "https://api.github.com/users/octocat/received_events",
         "type": "User",
         "site_admin": false
        }
       }
      ]
     }
    ]
    ```


=== "404 Not Found"

    Resource Not Found

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


