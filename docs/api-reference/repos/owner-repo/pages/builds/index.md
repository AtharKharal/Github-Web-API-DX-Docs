# builds

API endpoints for builds.

## Endpoints


### [List GitHub Pages builds](list-github-pages-builds.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/pages/builds?per_page=30&page=1`

...


### [Request a GitHub Pages build](request-a-github-pages-build.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/pages/builds`

You can request that your site be built from the latest revision on the default branch. This has the...


### [Get latest Pages build](get-latest-pages-build.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/pages/builds/latest`

...


### [Get GitHub Pages build](get-github-pages-build.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/pages/builds/:build_id`

...

