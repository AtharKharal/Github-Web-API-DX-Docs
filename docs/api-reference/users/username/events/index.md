# events

API endpoints for events.

## Endpoints


### [List events for the authenticated user](list-events-for-the-authenticated-user.md)

`GET` `{{baseUrl}}/users/:username/events?per_page=30&page=1`

If you are authenticated as the given user, you will see your private events. Otherwise, you'll only...


### [List organization events for the authenticated user](list-organization-events-for-the-authenticated-user.md)

`GET` `{{baseUrl}}/users/:username/events/orgs/:org?per_page=30&page=1`

This is the user's organization dashboard. You must be authenticated as the user to view this....


### [List public events for a user](list-public-events-for-a-user.md)

`GET` `{{baseUrl}}/users/:username/events/public?per_page=30&page=1`

...

