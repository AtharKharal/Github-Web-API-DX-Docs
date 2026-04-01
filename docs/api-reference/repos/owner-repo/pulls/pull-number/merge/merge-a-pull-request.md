# Merge a pull request

This endpoint triggers [notifications](https://help.github.com/articles/about-notifications/). Creating content too quickly using this endpoint may result in abuse rate limiting. See "[Abuse rate limits](https://developer.github.com/v3/#abuse-rate-limits)" and "[Dealing with abuse rate limits](https://developer.github.com/v3/guides/best-practices-for-integrators/#dealing-with-abuse-rate-limits)" for details.

```http
PUT {{baseUrl}}/repos/:owner/:repo/pulls/:pull_number/merge
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `pull_number` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    {
        "commit_title": "<string>",
        "commit_message": "<string>",
        "sha": "<string>",
        "merge_method": "<string>"
    }
    ```


## Responses


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


=== "409 Conflict"

    Response if sha was provided and pull request head did not match

    ```json
    {
     "message": "Head branch was modified. Review and try the merge again.",
     "documentation_url": "https://developer.github.com/v3/pulls/#merge-a-pull-request-merge-button"
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


=== "403 Forbidden"

    Forbidden

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "405 Method Not Allowed"

    Response if merge cannot be performed

    ```json
    {
     "message": "Pull Request is not mergeable",
     "documentation_url": "https://developer.github.com/v3/pulls/#merge-a-pull-request-merge-button"
    }
    ```


=== "200 OK"

    Response if merge was successful

    ```json
    {
     "sha": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
     "merged": true,
     "message": "Pull Request successfully merged"
    }
    ```


