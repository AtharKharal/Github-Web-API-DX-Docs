# {review id}

API endpoints for {review id}.

## Endpoints


### [Get a review for a pull request](get-a-review-for-a-pull-request.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/pulls/:pull_number/reviews/:review_id`

...


### [Update a review for a pull request](update-a-review-for-a-pull-request.md)

`PUT` `{{baseUrl}}/repos/:owner/:repo/pulls/:pull_number/reviews/:review_id`

Update the review summary comment with new text....


### [Delete a pending review for a pull request](delete-a-pending-review-for-a-pull-request.md)

`DELETE` `{{baseUrl}}/repos/:owner/:repo/pulls/:pull_number/reviews/:review_id`

...


### [List comments for a pull request review](list-comments-for-a-pull-request-review.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/pulls/:pull_number/reviews/:review_id/comments?per_page=30&page=1`

List comments for a specific pull request review....


### [Dismiss a review for a pull request](dismiss-a-review-for-a-pull-request.md)

`PUT` `{{baseUrl}}/repos/:owner/:repo/pulls/:pull_number/reviews/:review_id/dismissals`

**Note:** To dismiss a pull request review on a [protected branch](https://developer.github.com/v3/r...


### [Submit a review for a pull request](submit-a-review-for-a-pull-request.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/pulls/:pull_number/reviews/:review_id/events`

...

