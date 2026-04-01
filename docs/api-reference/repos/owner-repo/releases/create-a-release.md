# Create a release

Users with push access to the repository can create a release.

This endpoint triggers [notifications](https://help.github.com/articles/about-notifications/). Creating content too quickly using this endpoint may result in abuse rate limiting. See "[Abuse rate limits](https://developer.github.com/v3/#abuse-rate-limits)" and "[Dealing with abuse rate limits](https://developer.github.com/v3/guides/best-practices-for-integrators/#dealing-with-abuse-rate-limits)" for details.

```http
POST {{baseUrl}}/repos/:owner/:repo/releases
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    {
        "tag_name": "<string>",
        "target_commitish": "<string>",
        "name": "<string>",
        "body": "<string>",
        "draft": false,
        "prerelease": false
    }
    ```


## Responses


=== "201 Created"

    response

    ```json
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


