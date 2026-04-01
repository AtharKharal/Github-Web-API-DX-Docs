# Search issues and pull requests

Find issues by state and keyword. This method returns up to 100 results [per page](https://developer.github.com/v3/#pagination).

When searching for issues, you can get text match metadata for the issue **title**, issue **body**, and issue **comment body** fields when you pass the `text-match` media type. For more details about how to receive highlighted
search results, see [Text match metadata](https://developer.github.com/v3/search/#text-match-metadata).

For example, if you want to find the oldest unresolved Python bugs on Windows. Your query might look something like this.

`q=windows+label:bug+language:python+state:open&sort=created&order=asc`

This query searches for the keyword `windows`, within any open issue that is labeled as `bug`. The search runs across repositories whose primary language is Python. The results are sorted by creation date in ascending order, whick means the oldest issues appear first in the search results.

```http
GET {{baseUrl}}/search/issues?q=<string>&sort=<string>&order=desc&per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `q` | `string` | `Query` | `No` | (Required) The query contains one or more search keywords and qualifiers. Qualifiers allow you to limit your search to specific areas of GitHub. The REST API supports the same qualifiers as GitHub.com. To learn more about the format of the query, see [Constructing a search query](https://developer.github.com/v3/search/#constructing-a-search-query). See "[Searching issues and pull requests](https://help.github.com/articles/searching-issues-and-pull-requests/)" for a detailed list of qualifiers. |

| `sort` | `string` | `Query` | `No` | Sorts the results of your query by the number of `comments`, `reactions`, `reactions-+1`, `reactions--1`, `reactions-smile`, `reactions-thinking_face`, `reactions-heart`, `reactions-tada`, or `interactions`. You can also sort results by how recently the items were `created` or `updated`, Default: [best match](https://developer.github.com/v3/search/#ranking-search-results) |

| `order` | `string` | `Query` | `No` | Determines whether the first search result returned is the highest number of matches (`desc`) or lowest number of matches (`asc`). This parameter is ignored unless you provide `sort`. |

| `per_page` | `string` | `Query` | `No` | Results per page (max 100) |

| `page` | `string` | `Query` | `No` | Page number of the results to fetch. |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "503 Service Unavailable"

    Service Unavailable

    ```json
    {
     "code": "nisi",
     "message": "enim amet nostrud",
     "documentation_url": "reprehenderit id"
    }
    ```


=== "200 OK"

    response

    ```json
    {
     "total_count": 280,
     "incomplete_results": false,
     "items": [
      {
       "url": "https://api.github.com/repos/batterseapower/pinyin-toolkit/issues/132",
       "repository_url": "https://api.github.com/repos/batterseapower/pinyin-toolkit",
       "labels_url": "https://api.github.com/repos/batterseapower/pinyin-toolkit/issues/132/labels{/name}",
       "comments_url": "https://api.github.com/repos/batterseapower/pinyin-toolkit/issues/132/comments",
       "events_url": "https://api.github.com/repos/batterseapower/pinyin-toolkit/issues/132/events",
       "html_url": "https://github.com/batterseapower/pinyin-toolkit/issues/132",
       "id": 35802,
       "node_id": "MDU6SXNzdWUzNTgwMg==",
       "number": 132,
       "title": "Line Number Indexes Beyond 20 Not Displayed",
       "user": {
        "login": "Nick3C",
        "id": 90254,
        "node_id": "MDQ6VXNlcjkwMjU0",
        "avatar_url": "https://secure.gravatar.com/avatar/934442aadfe3b2f4630510de416c5718?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png",
        "gravatar_id": "",
        "url": "https://api.github.com/users/Nick3C",
        "html_url": "https://github.com/Nick3C",
        "followers_url": "https://api.github.com/users/Nick3C/followers",
        "following_url": "https://api.github.com/users/Nick3C/following{/other_user}",
        "gists_url": "https://api.github.com/users/Nick3C/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/Nick3C/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/Nick3C/subscriptions",
        "organizations_url": "https://api.github.com/users/Nick3C/orgs",
        "repos_url": "https://api.github.com/users/Nick3C/repos",
        "events_url": "https://api.github.com/users/Nick3C/events{/privacy}",
        "received_events_url": "https://api.github.com/users/Nick3C/received_events",
        "type": "User",
        "site_admin": true
       },
       "labels": [
        {
         "id": 4,
         "node_id": "MDU6TGFiZWw0",
         "url": "https://api.github.com/repos/batterseapower/pinyin-toolkit/labels/bug",
         "name": "bug",
         "color": "ff0000"
        }
       ],
       "state": "open",
       "assignee": null,
       "milestone": {
        "url": "https://api.github.com/repos/octocat/Hello-World/milestones/1",
        "html_url": "https://github.com/octocat/Hello-World/milestones/v1.0",
        "labels_url": "https://api.github.com/repos/octocat/Hello-World/milestones/1/labels",
        "id": 1002604,
        "node_id": "MDk6TWlsZXN0b25lMTAwMjYwNA==",
        "number": 1,
        "state": "open",
        "title": "v1.0",
        "description": "Tracking milestone for version 1.0",
        "creator": {
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
        "open_issues": 4,
        "closed_issues": 8,
        "created_at": "2011-04-10T20:09:31Z",
        "updated_at": "2014-03-03T18:58:10Z",
        "closed_at": "2013-02-12T13:22:01Z",
        "due_on": "2012-10-09T23:39:01Z"
       },
       "comments": 15,
       "created_at": "2009-07-12T20:10:41Z",
       "updated_at": "2009-07-19T09:23:43Z",
       "closed_at": null,
       "pull_request": {
        "url": "https://api/github.com/repos/octocat/Hello-World/pull/1347",
        "html_url": "https://github.com/octocat/Hello-World/pull/1347",
        "diff_url": "https://github.com/octocat/Hello-World/pull/1347.diff",
        "patch_url": "https://api.github.com/repos/octocat/Hello-World/pulls/1347"
       },
       "body": "...",
       "score": 1,
       "locked": true,
       "author_association": "collaborator"
      }
     ]
    }
    ```


=== "403 Forbidden"

    Forbidden

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "304 Not Modified"

    Not Modified

    ```json
    
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


