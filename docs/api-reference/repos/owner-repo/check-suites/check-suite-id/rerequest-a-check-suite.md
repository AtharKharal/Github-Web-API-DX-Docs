# Rerequest a check suite

Triggers GitHub to rerequest an existing check suite, without pushing new code to a repository. This endpoint will trigger the [`check_suite` webhook](https://developer.github.com/webhooks/event-payloads/#check_suite) event with the action `rerequested`. When a check suite is `rerequested`, its `status` is reset to `queued` and the `conclusion` is cleared.

To rerequest a check suite, your GitHub App must have the `checks:read` permission on a private repository or pull access to a public repository.

```http
POST {{baseUrl}}/repos/:owner/:repo/check-suites/:check_suite_id/rerequest
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `check_suite_id` | `string` | `Path` | `Yes` | (Required) check_suite_id parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "201 Created"

    response

    ```json
    
    ```


