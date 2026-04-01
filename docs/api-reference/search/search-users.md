# Search users

Find users via various criteria. This method returns up to 100 results [per page](https://developer.github.com/v3/#pagination).

When searching for users, you can get text match metadata for the issue **login**, **email**, and **name** fields when you pass the `text-match` media type. For more details about highlighting search results, see [Text match metadata](https://developer.github.com/v3/search/#text-match-metadata). For more details about how to receive highlighted search results, see [Text match metadata](https://developer.github.com/v3/search/#text-match-metadata).

For example, if you're looking for a list of popular users, you might try this query:

`q=tom+repos:%3E42+followers:%3E1000`

This query searches for users with the name `tom`. The results are restricted to users with more than 42 repositories and over 1,000 followers.

```http
GET {{baseUrl}}/search/users?q=<string>&sort=<string>&order=desc&per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `q` | `string` | `Query` | `No` | (Required) The query contains one or more search keywords and qualifiers. Qualifiers allow you to limit your search to specific areas of GitHub. The REST API supports the same qualifiers as GitHub.com. To learn more about the format of the query, see [Constructing a search query](https://developer.github.com/v3/search/#constructing-a-search-query). See "[Searching users](https://help.github.com/articles/searching-users/)" for a detailed list of qualifiers. |

| `sort` | `string` | `Query` | `No` | Sorts the results of your query by number of `followers` or `repositories`, or when the person `joined` GitHub. Default: [best match](https://developer.github.com/v3/search/#ranking-search-results) |

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


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


=== "200 OK"

    response

    ```json
    {
     "total_count": 12,
     "incomplete_results": false,
     "items": [
      {
       "login": "mojombo",
       "id": 1,
       "node_id": "MDQ6VXNlcjE=",
       "avatar_url": "https://secure.gravatar.com/avatar/25c7c18223fb42a4c6ae1c8db6f50f9b?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png",
       "gravatar_id": "",
       "url": "https://api.github.com/users/mojombo",
       "html_url": "https://github.com/mojombo",
       "followers_url": "https://api.github.com/users/mojombo/followers",
       "subscriptions_url": "https://api.github.com/users/mojombo/subscriptions",
       "organizations_url": "https://api.github.com/users/mojombo/orgs",
       "repos_url": "https://api.github.com/users/mojombo/repos",
       "received_events_url": "https://api.github.com/users/mojombo/received_events",
       "type": "User",
       "score": 1,
       "following_url": "https://api.github.com/users/mojombo/following{/other_user}",
       "gists_url": "https://api.github.com/users/mojombo/gists{/gist_id}",
       "starred_url": "https://api.github.com/users/mojombo/starred{/owner}{/repo}",
       "events_url": "https://api.github.com/users/mojombo/events{/privacy}",
       "site_admin": true
      }
     ]
    }
    ```


