# List commits on a pull request

Lists a maximum of 250 commits for a pull request. To receive a complete commit list for pull requests with more than 250 commits, use the [List commits](https://developer.github.com/v3/repos/commits/#list-commits) endpoint.

```http
GET {{baseUrl}}/repos/:owner/:repo/pulls/:pull_number/commits?per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `pull_number` | `string` | `Path` | `Yes` | (Required)  |

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
      "id": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
      "tree_id": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
      "message": "Fix all the bugs",
      "timestamp": "2016-10-10T00:00:00Z",
      "author": {
       "name": "Monalisa Octocat",
       "email": "mona@github.com"
      },
      "committer": {
       "name": "Monalisa Octocat",
       "email": "mona@github.com"
      }
     },
     {
      "id": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
      "tree_id": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
      "message": "Fix all the bugs",
      "timestamp": "2016-10-10T00:00:00Z",
      "author": {
       "name": "Monalisa Octocat",
       "email": "mona@github.com"
      },
      "committer": {
       "name": "Monalisa Octocat",
       "email": "mona@github.com"
      }
     }
    ]
    ```


