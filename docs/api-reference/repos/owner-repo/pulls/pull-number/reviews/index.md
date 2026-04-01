# reviews

API endpoints for reviews.

## Endpoints


### [{review id}](review-id/index.md)

`` ``




### [List reviews for a pull request](list-reviews-for-a-pull-request.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/pulls/:pull_number/reviews?per_page=30&page=1`

The list of reviews returns in chronological order....


### [Create a review for a pull request](create-a-review-for-a-pull-request.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/pulls/:pull_number/reviews`

This endpoint triggers [notifications](https://help.github.com/articles/about-notifications/). Creat...

