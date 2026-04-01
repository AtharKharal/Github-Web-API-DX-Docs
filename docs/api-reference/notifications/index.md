# notifications

API endpoints for notifications.

## Endpoints


### [threads/{thread id}](threads-thread-id/index.md)

`` ``




### [List notifications for the authenticated user](list-notifications-for-the-authenticated-user.md)

`GET` `{{baseUrl}}/notifications?all=false&participating=false&since=<string>&before=<string>&per_page=30&page=1`

List all notifications for the current user, sorted by most recently updated....


### [Mark notifications as read](mark-notifications-as-read.md)

`PUT` `{{baseUrl}}/notifications`

Marks all notifications as "read" removes it from the [default view on GitHub](https://github.com/no...

