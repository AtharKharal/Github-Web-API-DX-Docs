# Mark notifications as read

Marks all notifications as "read" removes it from the [default view on GitHub](https://github.com/notifications). If the number of notifications is too large to complete in one request, you will receive a `202 Accepted` status and GitHub will run an asynchronous process to mark notifications as "read." To check whether any "unread" notifications remain, you can use the [List notifications for the authenticated user](https://developer.github.com/v3/activity/notifications/#list-notifications-for-the-authenticated-user) endpoint and pass the query parameter `all=false`.

```http
PUT {{baseUrl}}/notifications
```





## Request Body

=== "JSON"

    ```json
    {
        "last_read_at": "<dateTime>",
        "read": "<boolean>"
    }
    ```


## Responses


=== "205 Reset Content"

    response

    ```json
    
    ```


=== "202 Accepted"

    response

    ```json
    {
     "message": "sed aliqua mollit cillum anim"
    }
    ```


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


=== "401 Unauthorized"

    Requires Authentication

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


