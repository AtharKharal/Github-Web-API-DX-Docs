# search

API endpoints for search.

## Endpoints


### [Search code](search-code.md)

`GET` `{{baseUrl}}/search/code?q=<string>&sort=<string>&order=desc&per_page=30&page=1`

Searches for query terms inside of a file. This method returns up to 100 results [per page](https://...


### [Search commits](search-commits.md)

`GET` `{{baseUrl}}/search/commits?q=<string>&sort=<string>&order=desc&per_page=30&page=1`

Find commits via various criteria on the default branch (usually `master`). This method returns up t...


### [Search issues and pull requests](search-issues-and-pull-requests.md)

`GET` `{{baseUrl}}/search/issues?q=<string>&sort=<string>&order=desc&per_page=30&page=1`

Find issues by state and keyword. This method returns up to 100 results [per page](https://developer...


### [Search labels](search-labels.md)

`GET` `{{baseUrl}}/search/labels?repository_id=<integer>&q=<string>&sort=<string>&order=desc`

Find labels in a repository with names or descriptions that match search keywords. Returns up to 100...


### [Search repositories](search-repositories.md)

`GET` `{{baseUrl}}/search/repositories?q=<string>&sort=<string>&order=desc&per_page=30&page=1`

Find repositories via various criteria. This method returns up to 100 results [per page](https://dev...


### [Search topics](search-topics.md)

`GET` `{{baseUrl}}/search/topics?q=<string>`

Find topics via various criteria. Results are sorted by best match. This method returns up to 100 re...


### [Search users](search-users.md)

`GET` `{{baseUrl}}/search/users?q=<string>&sort=<string>&order=desc&per_page=30&page=1`

Find users via various criteria. This method returns up to 100 results [per page](https://developer....

