# {username}

API endpoints for {username}.

## Endpoints


### [Check if a person is followed by the authenticated user](check-if-a-person-is-followed-by-the-authenticated-user.md)

`GET` `{{baseUrl}}/user/following/:username`

...


### [Follow a user](follow-a-user.md)

`PUT` `{{baseUrl}}/user/following/:username`

Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more in...


### [Unfollow a user](unfollow-a-user.md)

`DELETE` `{{baseUrl}}/user/following/:username`

Unfollowing a user requires the user to be logged in and authenticated with basic auth or OAuth with...

