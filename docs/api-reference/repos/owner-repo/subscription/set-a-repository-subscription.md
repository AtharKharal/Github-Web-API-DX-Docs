# Set a repository subscription

If you would like to watch a repository, set `subscribed` to `true`. If you would like to ignore notifications made within a repository, set `ignored` to `true`. If you would like to stop watching a repository, [delete the repository's subscription](https://developer.github.com/v3/activity/watching/#delete-a-repository-subscription) completely.

```http
PUT {{baseUrl}}/repos/:owner/:repo/subscription
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    {
        "subscribed": "<boolean>",
        "ignored": "<boolean>"
    }
    ```


## Responses


=== "200 OK"

    response

    ```json
    {
     "subscribed": true,
     "ignored": false,
     "reason": null,
     "created_at": "2012-10-06T21:34:12Z",
     "url": "https://api.github.com/repos/octocat/example/subscription",
     "repository_url": "https://api.github.com/repos/octocat/example"
    }
    ```


