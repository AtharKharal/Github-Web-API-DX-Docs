# check-suites

API endpoints for check-suites.

## Endpoints


### [{check suite id}](check-suite-id/index.md)

`` ``




### [Create a check suite](create-a-check-suite.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/check-suites`

**Note:** The Checks API only looks for pushes in the repository where the check suite or check run ...


### [Update repository preferences for check suites](update-repository-preferences-for-check-suites.md)

`PATCH` `{{baseUrl}}/repos/:owner/:repo/check-suites/preferences`

Changes the default automatic flow when creating check suites. By default, a check suite is automati...

