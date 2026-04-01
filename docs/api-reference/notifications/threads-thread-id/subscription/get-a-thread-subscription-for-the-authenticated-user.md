# Get a thread subscription for the authenticated user

This checks to see if the current user is subscribed to a thread. You can also [get a repository subscription](https://developer.github.com/v3/activity/watching/#get-a-repository-subscription).

Note that subscriptions are only generated if a user is participating in a conversation--for example, they've replied to the thread, were **@mentioned**, or manually subscribe to a thread.

```http
GET {{baseUrl}}/notifications/threads/:thread_id/subscription
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `thread_id` | `string` | `Path` | `Yes` | (Required) thread_id parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


=== "403 Forbidden"

    Forbidden

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "200 OK"

    response

    ```json
    {
     "subscribed": true,
     "ignored": false,
     "reason": null,
     "created_at": "2012-10-06T21:34:12Z",
     "url": "https://api.github.com/notifications/threads/1/subscription",
     "thread_url": "https://api.github.com/notifications/threads/1"
    }
    ```


=== "401 Unauthorized"

    Requires Authentication

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


