# plans

API endpoints for plans.

## Endpoints


### [List plans (stubbed)](list-plans-(stubbed).md)

`GET` `{{baseUrl}}/marketplace_listing/stubbed/plans?per_page=30&page=1`

Lists all plans that are part of your GitHub Marketplace listing.

GitHub Apps must use a [JWT](http...


### [List accounts for a plan (stubbed)](list-accounts-for-a-plan-(stubbed).md)

`GET` `{{baseUrl}}/marketplace_listing/stubbed/plans/:plan_id/accounts?sort=created&direction=<string>&per_page=30&page=1`

Returns repository and organization accounts associated with the specified plan, including free plan...

