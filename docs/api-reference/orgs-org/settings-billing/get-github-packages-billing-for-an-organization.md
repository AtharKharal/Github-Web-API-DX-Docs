# Get GitHub Packages billing for an organization

**Warning:** The Billing API is currently in public beta and subject to change.

Gets the free and paid storage usued for GitHub Packages in gigabytes.

Paid minutes only apply to packages stored for private repositories. For more information, see "[Managing billing for GitHub Packages](https://help.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages)."

Access tokens must have the `read:org` scope.

```http
GET {{baseUrl}}/orgs/:org/settings/billing/packages
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `org` | `string` | `Path` | `Yes` | (Required)  |



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


