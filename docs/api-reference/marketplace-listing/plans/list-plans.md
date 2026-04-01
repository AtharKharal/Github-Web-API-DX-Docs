# List plans

Lists all plans that are part of your GitHub Marketplace listing.

GitHub Apps must use a [JWT](https://developer.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. OAuth Apps must use [basic authentication](https://developer.github.com/v3/auth/#basic-authentication) with their client ID and client secret to access this endpoint.

```http
GET {{baseUrl}}/marketplace_listing/plans?per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `per_page` | `string` | `Query` | `No` | Results per page (max 100) |

| `page` | `string` | `Query` | `No` | Page number of the results to fetch. |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "401 Unauthorized"

    Requires Authentication

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "200 OK"

    response

    ```json
    [
     {
      "url": "https://api.github.com/marketplace_listing/plans/1313",
      "accounts_url": "https://api.github.com/marketplace_listing/plans/1313/accounts",
      "id": 1313,
      "number": 3,
      "name": "Pro",
      "description": "A professional-grade CI solution",
      "monthly_price_in_cents": 1099,
      "yearly_price_in_cents": 11870,
      "price_model": "flat-rate",
      "has_free_trial": true,
      "unit_name": null,
      "state": "published",
      "bullets": [
       "Up to 25 private repositories",
       "11 concurrent builds"
      ]
     }
    ]
    ```


=== "404 Not Found"

    Resource Not Found

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


