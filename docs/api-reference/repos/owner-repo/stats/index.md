# stats

API endpoints for stats.

## Endpoints


### [Get the weekly commit activity](get-the-weekly-commit-activity.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/stats/code_frequency`

Returns a weekly aggregate of the number of additions and deletions pushed to a repository....


### [Get the last year of commit activity](get-the-last-year-of-commit-activity.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/stats/commit_activity`

Returns the last year of commit activity grouped by week. The `days` array is a group of commits per...


### [Get all contributor commit activity](get-all-contributor-commit-activity.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/stats/contributors`


Returns the `total` number of commits authored by the contributor. In addition, the response includ...


### [Get the weekly commit count](get-the-weekly-commit-count.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/stats/participation`

Returns the total commit counts for the `owner` and total commit counts in `all`. `all` is everyone ...


### [Get the hourly commit count for each day](get-the-hourly-commit-count-for-each-day.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/stats/punch_card`

Each array contains the day number, hour number, and number of commits:

*   `0-6`: Sunday - Saturda...

