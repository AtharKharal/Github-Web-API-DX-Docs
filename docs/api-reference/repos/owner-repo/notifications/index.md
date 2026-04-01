# notifications

API endpoints for notifications.

## Endpoints


### [List repository notifications for the authenticated user](list-repository-notifications-for-the-authenticated-user.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/notifications?all=false&participating=false&since=<string>&before=<string>&per_page=30&page=1`

List all notifications for the current user....


### [Mark repository notifications as read](mark-repository-notifications-as-read.md)

`PUT` `{{baseUrl}}/repos/:owner/:repo/notifications`

Marks all notifications in a repository as "read" removes them from the [default view on GitHub](htt...

