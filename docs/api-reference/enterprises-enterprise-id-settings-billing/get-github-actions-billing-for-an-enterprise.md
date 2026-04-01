# Get GitHub Actions billing for an enterprise

**Warning:** The Billing API is currently in public beta and subject to change.

Gets the summary of the free and paid GitHub Actions minutes used.

Paid minutes only apply to workflows in private repositories that use GitHub-hosted runners. Minutes used is listed for each GitHub-hosted runner operating system. Any job re-runs are also included in the usage. The usage does not include the multiplier for macOS and Windows runners and is not rounded up to the nearest whole minute. For more information, see "[Managing billing for GitHub Actions](https://help.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-actions)".

The authenticated user must be an enterprise admin.

```http
GET {{baseUrl}}/enterprises/:enterprise_id/settings/billing/actions
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `enterprise_id` | `string` | `Path` | `Yes` | (Required) Unique identifier of the GitHub Enterprise Cloud instance. |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "200 OK"

    response

    ```json
    {
     "total_minutes_used": 305,
     "total_paid_minutes_used": 0,
     "included_minutes": 3000,
     "minutes_used_breakdown": {
      "UBUNTU": 205,
      "MACOS": 10,
      "WINDOWS": 90
     }
    }
    ```


