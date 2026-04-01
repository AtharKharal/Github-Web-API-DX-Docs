# List check run annotations

Lists annotations for a check run using the annotation `id`. GitHub Apps must have the `checks:read` permission on a private repository or pull access to a public repository to get annotations for a check run. OAuth Apps and authenticated users must have the `repo` scope to get annotations for a check run in a private repository.

```http
GET {{baseUrl}}/repos/:owner/:repo/check-runs/:check_run_id/annotations?per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `check_run_id` | `string` | `Path` | `Yes` | (Required) check_run_id parameter |

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
      "path": "README.md",
      "start_line": 2,
      "end_line": 2,
      "start_column": 5,
      "end_column": 10,
      "annotation_level": "warning",
      "title": "Spell Checker",
      "message": "Check your spelling for 'banaas'.",
      "raw_details": "Do you mean 'bananas' or 'banana'?",
      "blob_href": "https://api.github.com/repos/github/rest-api-description/git/blobs/abc"
     }
    ]
    ```


