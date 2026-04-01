# subscription

API endpoints for subscription.

## Endpoints


### [Get a thread subscription for the authenticated user](get-a-thread-subscription-for-the-authenticated-user.md)

`GET` `{{baseUrl}}/notifications/threads/:thread_id/subscription`

This checks to see if the current user is subscribed to a thread. You can also [get a repository sub...


### [Set a thread subscription](set-a-thread-subscription.md)

`PUT` `{{baseUrl}}/notifications/threads/:thread_id/subscription`

If you are watching a repository, you receive notifications for all threads by default. Use this end...


### [Delete a thread subscription](delete-a-thread-subscription.md)

`DELETE` `{{baseUrl}}/notifications/threads/:thread_id/subscription`

Mutes all future notifications for a conversation until you comment on the thread or get an **@menti...

