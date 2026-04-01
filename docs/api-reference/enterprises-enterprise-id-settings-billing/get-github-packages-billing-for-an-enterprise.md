# Get GitHub Packages billing for an enterprise

**Warning:** The Billing API is currently in public beta and subject to change.

Gets the free and paid storage used for GitHub Packages in gigabytes.

Paid minutes only apply to packages stored for private repositories. For more information, see "[Managing billing for GitHub Packages](https://help.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages)."

The authenticated user must be an enterprise admin.

```http
GET {{baseUrl}}/enterprises/:enterprise_id/settings/billing/packages
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
     "total_gigabytes_bandwidth_used": 50,
     "total_paid_gigabytes_bandwidth_used": 40,
     "included_gigabytes_bandwidth": 10
    }
    ```


