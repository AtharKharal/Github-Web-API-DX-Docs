# Get shared storage billing for an enterprise

**Warning:** The Billing API is currently in public beta and subject to change.

Gets the estimated paid and estimated total storage used for GitHub Actions and Github Packages.

Paid minutes only apply to packages stored for private repositories. For more information, see "[Managing billing for GitHub Packages](https://help.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages)."

The authenticated user must be an enterprise admin.

```http
GET {{baseUrl}}/enterprises/:enterprise_id/settings/billing/shared-storage
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
     "days_left_in_billing_cycle": 20,
     "estimated_paid_storage_for_month": 15,
     "estimated_storage_for_month": 40
    }
    ```


