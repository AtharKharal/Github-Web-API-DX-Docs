# Re-run a workflow

Re-runs your workflow run using its `id`. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `actions:write` permission to use this endpoint.

```http
POST {{baseUrl}}/repos/:owner/:repo/actions/runs/:run_id/rerun
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `run_id` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "201 Created"

    response

    ```json
    
    ```


