# Set a thread subscription

If you are watching a repository, you receive notifications for all threads by default. Use this endpoint to ignore future notifications for threads until you comment on the thread or get an **@mention**.

You can also use this endpoint to subscribe to threads that you are currently not receiving notifications for or to subscribed to threads that you have previously ignored.

Unsubscribing from a conversation in a repository that you are not watching is functionally equivalent to the [Delete a thread subscription](https://developer.github.com/v3/activity/notifications/#delete-a-thread-subscription) endpoint.

```http
PUT {{baseUrl}}/notifications/threads/:thread_id/subscription
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `thread_id` | `string` | `Path` | `Yes` | (Required) thread_id parameter |



## Request Body

=== "JSON"

    ```json
    {
        "ignored": false
    }
    ```


## Responses


=== "403 Forbidden"

    Forbidden

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


=== "401 Unauthorized"

    Requires Authentication

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


