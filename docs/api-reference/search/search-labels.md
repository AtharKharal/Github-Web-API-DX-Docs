# Search labels

Find labels in a repository with names or descriptions that match search keywords. Returns up to 100 results [per page](https://developer.github.com/v3/#pagination).

When searching for labels, you can get text match metadata for the label **name** and **description** fields when you pass the `text-match` media type. For more details about how to receive highlighted search results, see [Text match metadata](https://developer.github.com/v3/search/#text-match-metadata).

For example, if you want to find labels in the `linguist` repository that match `bug`, `defect`, or `enhancement`. Your query might look like this:

`q=bug+defect+enhancement&repository_id=64778136`

The labels that best match the query appear first in the search results.

```http
GET {{baseUrl}}/search/labels?repository_id=<integer>&q=<string>&sort=<string>&order=desc
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `repository_id` | `string` | `Query` | `No` | (Required) The id of the repository. |

| `q` | `string` | `Query` | `No` | (Required) The search keywords. This endpoint does not accept qualifiers in the query. To learn more about the format of the query, see [Constructing a search query](https://developer.github.com/v3/search/#constructing-a-search-query). |

| `sort` | `string` | `Query` | `No` | Sorts the results of your query by when the label was `created` or `updated`. Default: [best match](https://developer.github.com/v3/search/#ranking-search-results) |

| `order` | `string` | `Query` | `No` | Determines whether the first search result returned is the highest number of matches (`desc`) or lowest number of matches (`asc`). This parameter is ignored unless you provide `sort`. |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "404 Not Found"

    Resource Not Found

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
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
     "total_count": 2,
     "incomplete_results": false,
     "items": [
      {
       "id": 418327088,
       "node_id": "MDU6TGFiZWw0MTgzMjcwODg=",
       "url": "https://api.github.com/repos/octocat/linguist/labels/enhancement",
       "name": "enhancement",
       "color": "84b6eb",
       "default": true,
       "description": "New feature or request.",
       "score": 1
      },
      {
       "id": 418327086,
       "node_id": "MDU6TGFiZWw0MTgzMjcwODY=",
       "url": "https://api.github.com/repos/octocat/linguist/labels/bug",
       "name": "bug",
       "color": "ee0701",
       "default": true,
       "description": "Something isn't working.",
       "score": 1
      }
     ]
    }
    ```


