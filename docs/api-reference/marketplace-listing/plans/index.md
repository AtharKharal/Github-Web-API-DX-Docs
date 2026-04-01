# plans

API endpoints for plans.

## Endpoints


### [List plans](list-plans.md)

`GET` `{{baseUrl}}/marketplace_listing/plans?per_page=30&page=1`

Lists all plans that are part of your GitHub Marketplace listing.

GitHub Apps must use a [JWT](http...


### [List accounts for a plan](list-accounts-for-a-plan.md)

`GET` `{{baseUrl}}/marketplace_listing/plans/:plan_id/accounts?sort=created&direction=<string>&per_page=30&page=1`

Returns user and organization accounts associated with the specified plan, including free plans. For...

