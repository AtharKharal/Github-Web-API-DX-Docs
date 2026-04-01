# List subscriptions for the authenticated user

Lists the active subscriptions for the authenticated user. You must use a [user-to-server OAuth access token](https://developer.github.com/apps/building-github-apps/identifying-and-authorizing-users-for-github-apps/#identifying-users-on-your-site), created for a user who has authorized your GitHub App, to access this endpoint. . OAuth Apps must authenticate using an [OAuth token](https://developer.github.com/apps/building-github-apps/authenticating-with-github-apps/).

```http
GET {{baseUrl}}/user/marketplace_purchases?per_page=30&page=1
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


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


=== "401 Unauthorized"

    Requires Authentication

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
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


=== "200 OK"

    response

    ```json
    [
     {
      "billing_cycle": "monthly",
      "next_billing_date": "2017-11-11T00:00:00Z",
      "unit_count": null,
      "on_free_trial": true,
      "free_trial_ends_on": "2017-11-11T00:00:00Z",
      "updated_at": "2017-11-02T01:12:12Z",
      "account": {
       "login": "github",
       "id": 4,
       "url": "https://api.github.com/orgs/github",
       "email": null,
       "organization_billing_email": "billing@github.com",
       "type": "Organization"
      },
      "plan": {
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
     }
    ]
    ```


