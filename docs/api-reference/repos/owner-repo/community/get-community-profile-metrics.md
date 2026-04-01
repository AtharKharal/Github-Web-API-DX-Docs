# Get community profile metrics

This endpoint will return all community profile metrics, including an overall health score, repository description, the presence of documentation, detected code of conduct, detected license, and the presence of ISSUE\_TEMPLATE, PULL\_REQUEST\_TEMPLATE, README, and CONTRIBUTING files.

```http
GET {{baseUrl}}/repos/:owner/:repo/community/profile
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "200 OK"

    response

    ```json
    {
     "health_percentage": 100,
     "description": "My first repository on GitHub!",
     "documentation": null,
     "files": {
      "code_of_conduct": {
       "name": "Contributor Covenant",
       "key": "contributor_covenant",
       "url": "https://api.github.com/codes_of_conduct/contributor_covenant",
       "html_url": "https://github.com/octocat/Hello-World/blob/master/CODE_OF_CONDUCT.md"
      },
      "contributing": {
       "url": "https://api.github.com/repos/octocat/Hello-World/contents/CONTRIBUTING",
       "html_url": "https://github.com/octocat/Hello-World/blob/master/CONTRIBUTING"
      },
      "issue_template": {
       "url": "https://api.github.com/repos/octocat/Hello-World/contents/ISSUE_TEMPLATE",
       "html_url": "https://github.com/octocat/Hello-World/blob/master/ISSUE_TEMPLATE"
      },
      "pull_request_template": {
       "url": "https://api.github.com/repos/octocat/Hello-World/contents/PULL_REQUEST_TEMPLATE",
       "html_url": "https://github.com/octocat/Hello-World/blob/master/PULL_REQUEST_TEMPLATE"
      },
      "license": {
       "name": "MIT License",
       "key": "mit",
       "spdx_id": "MIT",
       "url": "https://api.github.com/licenses/mit",
       "html_url": "https://github.com/octocat/Hello-World/blob/master/LICENSE",
       "node_id": "MDc6TGljZW5zZW1pdA=="
      },
      "readme": {
       "url": "https://api.github.com/repos/octocat/Hello-World/contents/README.md",
       "html_url": "https://github.com/octocat/Hello-World/blob/master/README.md"
      }
     },
     "updated_at": "2017-02-28T19:09:29Z"
    }
    ```


