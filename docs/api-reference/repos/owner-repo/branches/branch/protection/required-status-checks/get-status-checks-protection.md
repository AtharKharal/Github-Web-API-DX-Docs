# Get status checks protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

```http
GET {{baseUrl}}/repos/:owner/:repo/branches/:branch/protection/required_status_checks
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
    
    ```


## Responses


=== "200 OK"

    response

    ```json
    {
     "url": "https://api.github.com/repos/octocat/Hello-World/branches/master/protection/required_status_checks",
     "strict": true,
     "contexts": [
      "continuous-integration/travis-ci"
     ],
     "contexts_url": "https://api.github.com/repos/octocat/Hello-World/branches/master/protection/required_status_checks/contexts"
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


