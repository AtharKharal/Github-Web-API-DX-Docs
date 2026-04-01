# List accounts for a plan (stubbed)

Returns repository and organization accounts associated with the specified plan, including free plans. For per-seat pricing, you see the list of accounts that have purchased the plan, including the number of seats purchased. When someone submits a plan change that won't be processed until the end of their billing cycle, you will also see the upcoming pending change.

GitHub Apps must use a [JWT](https://developer.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. OAuth Apps must use [basic authentication](https://developer.github.com/v3/auth/#basic-authentication) with their client ID and client secret to access this endpoint.

```http
GET {{baseUrl}}/marketplace_listing/stubbed/plans/:plan_id/accounts?sort=created&direction=<string>&per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `plan_id` | `string` | `Path` | `Yes` | (Required) plan_id parameter |

| `sort` | `string` | `Query` | `No` | One of `created` (when the repository was starred) or `updated` (when it was last pushed to). |

| `direction` | `string` | `Query` | `No` | To return the oldest accounts first, set to `asc`. Can be one of `asc` or `desc`. Ignored without the `sort` parameter. |

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
      "url": "https://api.github.com/orgs/github",
      "type": "Organization",
      "id": 4,
      "login": "github",
      "organization_billing_email": "billing@github.com",
      "marketplace_pending_change": {
       "effective_date": "2017-11-11T00:00:00Z",
       "unit_count": null,
       "id": 77,
       "plan": {
        "url": "https://api.github.com/marketplace_listing/plans/1111",
        "accounts_url": "https://api.github.com/marketplace_listing/plans/1111/accounts",
        "id": 1111,
        "number": 2,
        "name": "Startup",
        "description": "A professional-grade CI solution",
        "monthly_price_in_cents": 699,
        "yearly_price_in_cents": 7870,
        "price_model": "flat-rate",
        "has_free_trial": true,
        "state": "published",
        "unit_name": null,
        "bullets": [
         "Up to 10 private repositories",
         "3 concurrent builds"
        ]
       }
      },
      "marketplace_purchase": {
       "billing_cycle": "monthly",
       "next_billing_date": "2017-11-11T00:00:00Z",
       "unit_count": null,
       "on_free_trial": true,
       "free_trial_ends_on": "2017-11-11T00:00:00Z",
       "updated_at": "2017-11-02T01:12:12Z",
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
     }
    ]
    ```


